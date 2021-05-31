from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineCheckboxes

from crispy_forms.layout import Submit, Layout, Field

UNIVERSITIES = (
    ('', 'Wybierz...'),
    ('NS', 'Nie studiuję'),
    ('WAT', 'Wojskowa Akademia Techniczna'),
    ('UW', 'Uniwersytet Warszawski'),
    ('PW', 'Politechnika Warszawska')
)

LANGUAGES = (
    ('1', 'Polski'),
    ('2', 'Angielski'),
    ('3', 'Hiszpański'),
    ('4', 'Rosyjski'),
    ('5', 'Francuski'),
    ('6', 'Japoński'),
    ('7', 'Czeski'),
    ('8', 'Grecki'),
    ('9', 'Koreański'),
    ('10', 'Turecki'),
    ('11', 'Włoski'),
    ('12', 'Niemiecki'),
    ('13', 'Chiński'),
    ('14', 'Wietnamski'),
)


class ApplicationForm(forms.Form):
    name = forms.CharField(label='Imię', max_length=100)
    surname = forms.CharField(label='Nazwisko', max_length=100)
    city = forms.CharField(label='Miasto', max_length=100)
    state = forms.CharField(label='Województwo', max_length=100)
    phoneNumber = forms.RegexField(label='Numer telefonu', regex=r'^\+?1?\d{9,15}$')
    emailAddress = forms.EmailField(label='Adres e-mail', max_length=100)
    university = forms.ChoiceField(label='Uniwersytet', choices=UNIVERSITIES)
    languages = forms.MultipleChoiceField(label='Języki', choices=LANGUAGES, widget=forms.CheckboxSelectMultiple)
    other_files_field = forms.FileField(label='Dodaj inne pliki', widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    CV_file = forms.CharField(label='CV', max_length=100, required=False)
    skills = forms.CharField(label = 'Skills', max_length=1000, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'application'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'name',
            'surname',
            'city',
            'state',
            'phoneNumber',
            'emailAddress',
            'university',
            InlineCheckboxes('languages'),
            'other_files_field',
            Field('CV_file', readonly=True),
            Field('skills', type='hidden')
        )
        self.helper.add_input(Submit('submit', 'Zatwierdź'))
