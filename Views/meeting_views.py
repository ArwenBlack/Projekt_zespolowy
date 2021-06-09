from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from Forms.meeting_form import MeetingForm
from Projekt_zespołowy.models import UserMeeting, PersonMeeting, Person, Meeting

# helpers


def save_usr_m(employees, meeting):
    for user in employees:
        new_user_meeting = UserMeeting(
            user=User.objects.get(id=int(user)),
            meeting=meeting
        )
        new_user_meeting.save()


# get initial data
def initial_data(meeting):
    candidate = ''
    users = []
    meetings = PersonMeeting.objects.all()
    usr_meetings = UserMeeting.objects.all()

    for person_meeting in meetings:
        if person_meeting.meeting == meeting:
            candidate = person_meeting.person.get_id()

    for usr_meeting in usr_meetings:
        if usr_meeting.meeting == meeting:
            users.append(str(usr_meeting.user.id))

    return {'date': meeting.start_time.date,
            'time': meeting.start_time.time,
            'descr': meeting.description,
            'title': meeting.title,
            'candidate': str(candidate),
            'user': users}


# get form data
def get_data(form):
    date = form.cleaned_data['date']
    time = form.cleaned_data['time']
    candidate = form.cleaned_data['candidate']
    employees = form.cleaned_data['user']
    title = form.cleaned_data['title']
    descr = form.cleaned_data['descr']
    return date, time, candidate, employees, title, descr


# save info
def save_meeting(meeting, candidate, employees):
    meeting.save()

    if candidate != '':
        meeting.is_free = False
        meeting.save()

        person_meeting = PersonMeeting(
            person=Person.objects.get(pk=candidate),
            meeting=meeting
        )

        person_meeting.save()

    if employees is not None:
        save_usr_m(employees, meeting)


def edit_meeting_view(request):
    meeting = Meeting.objects.get(pk=request.GET.get('meeting', ''))

    if request.method == 'POST':
        form = MeetingForm(request.POST, initial=initial_data(meeting))
        if form.is_valid():
            date, time, candidate, employees, title, descr = get_data(form)

            meeting.title = title
            meeting.description=descr
            meeting.start_time = datetime.combine(date, time)
            meeting.is_free=True
            save_meeting(meeting, candidate, employees)

            return redirect('calendar')

    else:
        form = MeetingForm(initial=initial_data(meeting))

    return render(request, 'meeting_form.html', {'form': form})


def new_meeting_view(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            date, time, candidate, employees, title, descr = get_data(form)

            meeting = Meeting(title=title, description=descr, start_time=datetime.combine(date, time), is_free=True)
            save_meeting(meeting, candidate, employees)

            return redirect('calendar')

    else:
        form = MeetingForm()

    return render(request, 'meeting_form.html', {'form': form})
