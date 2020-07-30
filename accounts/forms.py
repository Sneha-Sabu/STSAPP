from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Entry, BlackList, Region
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _


choices = [('americas', 'Americas'),('uk','UK'),('north_west_europe','North West Europe'),('mediterranean','Mediterranean'), ('west_africa','West Africa'),('south_africa','South Africa'), ('middle_east','Middle East'), ('indian_subcontinent','Indian Subcontinent'), ('asia_pacific','Asia Pacific')]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('number_of_images', 'region',)
        help_texts = {
            'Location_Name': _(
                'Enter the Location Name without any special characters e.g. comma(,), hifen (-), etc.'),
            'degrees_latitude': _(
                'Enter the positive degree value for East and North direction; enter the negative degree value for South and West direction.'),
            'degrees_longitude': _(
                'Enter the positive degree value for East and North direction; enter the negative degree value for South and West direction.'),
            'minutes_latitude': _('Enter "0" or the rounded up minutes without decimals.'),
            'minutes_longitude': _('Enter "0" or the rounded up minutes without decimals.'),
            'seconds_latitude': _('Enter "0" or the rounded up seconds without decimals.'),
            'seconds_longitude': _('Enter "0" or the rounded up seconds without decimals.'),
            'STS_Latitude': _(
                'Do not enter any values here. Decimal conversion will be done automatically by the system'),
            'STS_Longitude': _(
                'Do not enter any values here. Decimal conversion will be done automatically by the system'),
        }
        widgets = {
            'number_of_images': forms.Select(choices=Entry.CHOICES),
            'region': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }