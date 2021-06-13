import os
import webbrowser
from collections import defaultdict
from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import loader, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from Forms.Cv_form import CVForm
from Forms.meeting_form import MeetingForm
from Functional_files.CV_analize import extract_from_CV
from Views.TestFiles.test_offer import first_offer
from Projekt_zespołowy.models import JobOffer, Person, Application, Education, PersonMeeting, UserMeeting, Meeting, \
    OpinionAboutCandidate

from Forms.application_form import ApplicationForm, LANGUAGES

from django.shortcuts import render, redirect
from Projekt_zespołowy.forms import NewUserForm, NewJobOfferForm
from django.contrib import messages
# LOGIN
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from Functional_files.mail_sender import mail_sender, set_email_content

check = 0


@csrf_protect
def main_page(request):
    data = JobOffer.objects.all()

    if request.method == 'POST':
        tags = request.POST.getlist('filter')
        data_filtered = []
        for x in data:
            for t in tags:
                if t in x.description:
                    data_filtered.append(x)
        # serialized_data = serializers.serialize('json', data)
        # return JsonResponse(serialized_data, safe=False)
        data = data_filtered

    return render(request, "startpage.html", {'data': data})


def offer_page(request, offer_title):
    offer = get_object_or_404(JobOffer, title=offer_title)
    template = loader.get_template('offer.html')
    context = {
        'offer': offer,
    }
    return HttpResponse(template.render(context, request))


def offer_page_test(request):
    # oferta testowa
    data = first_offer
    if request.method == 'POST':
        return render(request, "application_page.html")

    return render(request, "offer.html", {'offer': data})


def handle_uploaded_file(f):
    with open('temp_data/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_protect
def CV_page(request, offer_title):
    if request.method == 'POST':
        if 'CV_submit' in request.POST:
            form = CVForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['CSV_field'])
                file = request.FILES['CSV_field']
                offer = JobOffer.objects.filter(title=offer_title)[0]
                data = extract_from_CV('temp_data/' + str(file), offer.requirements)
                print(data)
                skills_char = ",".join(data[4])
                f = ApplicationForm(
                    initial={'name': data[0], 'surname': data[1], 'phoneNumber': data[2], 'emailAddress': data[3],
                             'skills': skills_char,
                             'CV_file': str(file)})
                print(skills_char)
                return render(request, "application_page.html", {'form': f})
        else:
            form = ApplicationForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                phone_number = form.cleaned_data['phoneNumber']
                email_adress = form.cleaned_data['emailAddress']
                university = form.cleaned_data['university']
                language = form.cleaned_data.get('languages')
                languages = []
                language_dict = dict(LANGUAGES)
                for n in language:
                    languages.append(str(language_dict[n]))
                skills = form.cleaned_data['skills']
                print(skills)
                offer = JobOffer.objects.filter(title=offer_title)[0]
                CV = 'temp_data/' + form.cleaned_data['CV_file']
                f = open(CV, 'rb')
                p = Person(name=name, secondName=surname, email=email_adress, phone=phone_number)
                a = Application(date=datetime.now(), file=f.read(), skills=skills, jobOffer=offer, person=p)
                e = Education(uni_name=university, languages=','.join(languages), application=a)
                p.save()
                a.save()
                f.close()
                e.save()
                os.remove(str(CV))
                return render(request, "application_sent.html")
            form = ApplicationForm()
            return render(request, "application_page.html", {'form': form})
    else:
        form = CVForm()

    return render(request, "CV_page.html", {'form': form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main_page")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request, "register.html", {"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main_page")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main_page")


def dashboard_page(request):
    return render(request, "dashboard.html")


def offer_manager(request):
    data = JobOffer.objects.all()
    context = {
        'offers': data
    }
    return render(request, "dashboard_offer_manager.html", context)


def offer_manager_add(request):
    if request.method == "POST":
        form = NewJobOfferForm(request.POST)
        if form.is_valid():
            form.save()

    form = NewJobOfferForm
    return render(request, "dashboard_offer_manager_add.html", {"new_job_offer": form})


def offer_manager_edit(request, id):
    instance = get_object_or_404(JobOffer, id=id)
    form = NewJobOfferForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('offerManager')
    return render(request, "dashboard_offer_manager_edit.html", {"new_job_offer": form})


def offer_manager_details(request, id):
    offer = get_object_or_404(JobOffer, id=id)
    template = loader.get_template('dashboard_offer_manager_details.html')
    context = {
        'offer': offer,
    }
    return HttpResponse(template.render(context, request))


def offer_manager_delete(request, offer_id):
    offer = get_object_or_404(JobOffer, id=offer_id)
    offer.delete()
    return redirect('offer_manager')


def offer_applications(request):
    data = JobOffer.objects.all()
    context = {
        'offers': data
    }
    return render(request, "dashboard_applications.html", context)


def offer_applications_details(request, id):
    offer = get_object_or_404(JobOffer, id=id)
    applications = Application.objects.all().filter(jobOffer=id);
    applications_and_opinions = {}

    for application in applications:
        opinion = OpinionAboutCandidate.objects.filter(application=application)
        if opinion.exists():
            applications_and_opinions[application] = opinion[0]
        else:
            applications_and_opinions[application] = None
    context = {
        'offer': offer,
        'applications': applications,
        'app_opinion': applications_and_opinions
    }

    return render(request, "dashboard_applications_details.html", context)


def offer_applications_person_details(request, id):
    application = get_object_or_404(Application, id=id)
    f = open(os.path.dirname(__file__) + '/../temp_data/temp_file.pdf', 'wb')
    CV_file = application.file
    f.write(CV_file)
    f.close()
    context = {
        'application': application
    }
    return render(request, "dashboard_applications_person_details.html", context)


def get_CV(request, id):
    webbrowser.open_new(os.path.dirname(__file__) + '/../temp_data/temp_file.pdf')
    return offer_applications_person_details(request,id)


def opinions_view(request, id):
    opinion = OpinionAboutCandidate.objects.all().get(pk=id)
    return render(request, "opinion_page.html", {'opinion': opinion})


def employ(request, id):
    opinion = OpinionAboutCandidate.objects.all().get(pk=id)
    email_content = set_email_content(opinion.candidate.name, opinion.application.jobOffer.title)
    mail_sender(email_content, "<nazwa firmy> zaprasza do współpracy.", opinion.candidate.email)
    return render(request, "opinion_page.html", {'opinion': opinion})
