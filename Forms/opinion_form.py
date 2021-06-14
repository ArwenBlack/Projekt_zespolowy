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


class OpinionForm(forms.Form):
    content = forms.CharField(label="Treść opinii o kandydacie", max_length=5000)
    user = forms.ChoiceField(label="Pracownik", choices=create_list_of_users())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "opinion"
        self.helper.form_method = "post"
        self.fields['user'].required = False
        self.helper.layout = Layout(
            'content',
            'user'
        )
        self.helper.add_input(Submit('submit', 'Zatwierdź'))