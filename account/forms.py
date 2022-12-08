from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from account.models import *

class AudienceUserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': "",
            'placeholder': "Enter username",
            'type': "text",
            'class': "form-control",
            'name': "username",
            'id': "username",
        })
        self.fields["first_name"].widget.attrs.update({
            'required': "",
            'placeholder': "Enter First Name",
            'type': "text",
            'class': "form-control",
            'name': "name",
            'id': "firs-name",
        })
        self.fields["last_name"].widget.attrs.update({
            'required': "",
            'placeholder': "Enter Last Name",
            'type': "text",
            'class': "form-control",
            'name': "name",
            'id': "last-name",
        })
        self.fields["email"].widget.attrs.update({
            'required': "",
            'placeholder': "Enter Email",
            'type': "email",
            'class': "form-control",
            'name': "email",
            'id': "email",
        })
        self.fields["password1"].widget.attrs.update({
            'required': "",
            'placeholder': "Please enter your password",
            'type': "password",
            'class': "form-control",
            'name': "password",
            'id': "password-1",
        })
        self.fields["password2"].widget.attrs.update({
            'required': "",
            'placeholder': "Enter password again",
            'type': "password",
            'class': "form-control",
            'name': "password",
            'id': "password-2",
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class editUserPofile(ModelForm):
    class Meta:
        model = UserSetting
        # Set the form fields
        fields = (
            'profile_picture','theme','education')
        labels = {
            'theme': 'Choose a Theme',
            "education": 'Education Level',
            "profile_picture":'Upload an image',
        }
        widgets = {

            'theme': forms.Select(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(
                attrs={'class': "form-control", 'multiple': True, }),

        }