from django.contrib import admin

from Projekt_zespołowy.models import Person
from Projekt_zespołowy.models import Meeting
from Projekt_zespołowy.models import PersonMeeting
from Projekt_zespołowy.models import JobOffer
from Projekt_zespołowy.models import Requirement
from Projekt_zespołowy.models import Application
from Projekt_zespołowy.models import Education
from Projekt_zespołowy.models import PromisingCandidate
from Projekt_zespołowy.models import OpinionAboutCandidate


admin.site.register(Person)
admin.site.register(Meeting)
admin.site.register(PersonMeeting)
admin.site.register(JobOffer)
admin.site.register(Requirement)
admin.site.register(Application)
admin.site.register(Education)
admin.site.register(PromisingCandidate)
admin.site.register(OpinionAboutCandidate)
