from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineCheckboxes

from crispy_forms.layout import Submit, Layout



class CVForm(forms.Form):
    CSV_field = forms.FileField(label='Dodaj CV', widget=forms.ClearableFileInput(attrs={'multiple': False}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'application'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'CSV_field'
        )
        self.helper.add_input(Submit('submit', 'Zatwierdź'))
