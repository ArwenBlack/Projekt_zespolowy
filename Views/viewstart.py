import base64
import os
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, loader, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
# dane testowe
from Forms.Cv_form import CVForm
from Functional_files.CV_analize import extract_from_CV
from Views.TestFiles.test_offer import first_offer
from Views.TestFiles.test_offeR_2 import second_offer
from Projekt_zespołowy.models import JobOffer, Person, Application

from Forms.application_form import ApplicationForm

check = 0


# dane testowe


# TODO: csrf protect
@csrf_exempt
def main_page(request):
    tags = []
    data = [first_offer, second_offer]
    if request.method == 'POST':
        # lista wpisanych i zatwierdzonych tagów
        req = request.POST.copy()
        tags = req.getlist('filterList[]')
        data_filtered = []
        for x in data:
            for t in tags:
                if t in x.description:
                    data_filtered.append(x)
        serialized_data = serializers.serialize('json', data)
        return JsonResponse(serialized_data, safe=False)
    # filtrowanie ofert na podstawie wpisanych tagów
    # tablica z ofertami, którą prześle się jako argument

    # data = JobOffer.objects.all()
    return render(request, "startpage.html", {'data': data})


def offer_page(request, offer_title):
    data = [first_offer, second_offer]
    offer = next(filter(lambda x: x.title == offer_title, data))
    template = loader.get_template('offer.html')
    context = {
        'offer': offer,
    }
    return HttpResponse(template.render(context, request))


def offer_page_test(request):
    # oferta testowa
    data = first_offer
    # dodać funkcję, która rozdziela dodatkowe korzyści i nice to have
    # na pojedyncze stringi tak jak w tej klasie testowej wyżej
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
                data = extract_from_CV('temp_data/' + str(file))
                f = ApplicationForm(
                    initial={'name': data[0], 'surname': data[1], 'phoneNumber': data[2], 'emailAddress': data[3],
                             'CV_file': str(file)})
                return render(request, "application_page.html", {'form': f})
        else:
            form = ApplicationForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                city = form.cleaned_data['city']
                phone_number = form.cleaned_data['phoneNumber']
                email_adress = form.cleaned_data['emailAddress']
                univercity = form.cleaned_data['university']
                language = form.cleaned_data['languages']
                print(offer_title)
                offer = JobOffer.objects.filter(title=offer_title)
                print(offer)
                CV = 'temp_data/' + form.cleaned_data['CV_file']
                f = open(CV, 'rb')
                p = Person(name=name, secondName=surname, email=email_adress, phone=phone_number)
                a = Application(date=datetime.now(), file=f.read(), skills = '',jobOffer=offer, person=p)
                p.save()
                a.save()
                f.close()
                os.remove(str(CV))
                return render(request, "application_sent.html")
            form = ApplicationForm()
            return render(request, "application_page.html", {'form': form})
    else:
        form = CVForm()

    return render(request, "CV_page.html", {'form': form})
