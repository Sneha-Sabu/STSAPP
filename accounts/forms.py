from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Entry, BlackList, Region

choices = [('asia', 'asia'),('africa','africa'),('north america','north america'),('south america','south america'), ('europe','europe'),('australia','australia')]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('number_of_images', 'region',)
        widgets = {
            'number_of_images': forms.Select(choices=Entry.CHOICES),
            'region': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }