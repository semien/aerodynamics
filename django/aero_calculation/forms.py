from django import forms
from .choices import *

from django_registration.forms import RegistrationForm

from .models import User


class MyRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User


class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=30)
    type = forms.ChoiceField(choices=PROJECT_TYPES, label="", initial='', widget=forms.Select(), required=True)



class AddForm(forms.Form):
    section = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 't_v | c | l | v | K ', 'aria-describedby': 'add-btn'}))
