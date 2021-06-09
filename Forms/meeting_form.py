from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.contrib.auth.models import User

from Projekt_zespołowy.models import Person


def create_list_of_candidates():
    candidates = [('', 'Wybierz...')]
    people = Person.objects.all()
    for person in people:
        element = [person.get_id(), person.get_name()]
        candidates.append(tuple(element))

    return tuple(candidates)


def create_list_of_users():
    all_users = []
    users = User.objects.all()
    for user in users:
        element = [str(user.id), user.username]
        all_users.append(tuple(element))

    return tuple(all_users)


class MeetingForm(forms.Form):
    title = forms.CharField(label="Nazwa spotkania", max_length=50)
    descr = forms.CharField(label="Opis spotkania", max_length=200)
    date = forms.DateField(label="Data spotkania", widget=forms.TextInput(
        attrs={'type': 'date'}
    ))
    time = forms.TimeField(label="Godzina spotkania", widget=forms.TextInput(
        attrs={'type': 'time'}
    ))
    candidate = forms.ChoiceField(label="Kandydat", choices=create_list_of_candidates())
    user = forms.MultipleChoiceField(
        label="Pracownik", choices=create_list_of_users(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "meeting"
        self.helper.form_method = "post"
        self.fields['candidate'].required = False
        self.fields['user'].required = False
        self.helper.layout = Layout(
            'title',
            'descr',
            'date',
            'time',
            'candidate',
            'user'
        )
        self.helper.add_input(Submit('submit', 'Zatwierdź'))