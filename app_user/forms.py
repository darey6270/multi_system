from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import UserProfile
from datetime import date

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    PAAS = "Paas"
    SAAS = "Saas"
    IAAS = "Iaas"

    SERVICES = (
        (PAAS, 'Platform as a Service (Paas)'),
        (SAAS, 'Software as a Service (Saas)'),
        (IAAS, 'Infrastructure as a Service (IAAS)'),
    )

    What_is_your_favourite_color = forms.CharField(max_length=23)
    Service_required = forms.ChoiceField(required=True, choices=SERVICES)

    class Meta:
        model = UserProfile
        fields = ('Date_of_Birth', 'Phone_number', 'Service_required', 'What_is_your_favourite_color')
        labels = {'Date_of_Birth': _('Date of Birth'), 'Phone_number': _('Phone number'),
                  'Service_required': _('Service Required'),
                  'What_is_your_favourite_color': ('What is your favourite color')}


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password'
        }

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2
