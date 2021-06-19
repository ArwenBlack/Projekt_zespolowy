from django.test import TestCase
from Projekt_zespołowy.models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="TestJan", secondName="Kowalski", email="kowalski@gmail.com", phone="123123123")

    def test_get_name(self):
        person = Person.objects.get(name="TestJan")
        self.assertEqual(person.get_name(), "Test Jan Kowalski")
