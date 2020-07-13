from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Entry, BlackList



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('number_of_images',)
        widgets = {
            'number_of_images': forms.Select(choices=Entry.CHOICES)
        }