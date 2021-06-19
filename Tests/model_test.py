from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from Projekt_zespołowy.models import Person, JobOffer
from Forms.opinion_form import OpinionForm


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="TestJan", secondName="Kowalski", email="kowalski@gmail.com", phone="123123123")

    def test_get_name(self):
        person = Person.objects.get(name="TestJan")
        self.assertEqual(person.get_name(), "TestJan Kowalski")


class JobOfferTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="admin")
        JobOffer.objects.create(
            title='TestCase', isActive=True, creation_date=datetime.now(),
            dueDate=datetime.now(), description='', bottomSalaryRange=0, upperSalaryRange=0,
            additionalBenefits='1,2,3', requirements='1,2,3', niceToHave='1,2,3', user=User.objects.get(username="admin")
        )

    def test_split(self):
        offer = JobOffer.objects.get(title="TestCase")
        self.assertEqual(offer.requirements_split(), ['1', '2', '3'])
        self.assertEqual(offer.benefits_split(), ['1', '2', '3'])
        self.assertEqual(offer.nicetohave_split(), ['1', '2', '3'])


