from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import *


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


class CreateStageForm(ModelForm):
    class Meta:
        model = Stage
        # Set the form fields
        fields = ('stage_name', 'stage_description', 'Stage_image')

        labels = {
            'stage_name': '',
            'stage_description': '',
            'Stage_image': ''
        }
        widgets = {
           
            'stage_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': 'Stage Name', 'id': 'stage-name'}),
            'stage_description': forms.Textarea(
                attrs={'class': "form-control", 'placeholder': 'Stage Description', 'id': 'stage-description'}),
            'Stage_image': forms.ClearableFileInput(
                attrs={'class': "form-control", 'multiple': True, 'id': 'stage-picture'}),
        }


class CreatePresentationForm(ModelForm):
    class Meta:
        model = Presentation
        StageSelection = forms.ModelChoiceField(queryset=Stage.objects.all())
        # Set the form fields
        fields = (
             'pres_name', 'pres_description', 'pres_file', 'pres_image', 'pres_date', 'stage', 'type')
        Choice_value = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]
        labels = {

            'pres_name': '',
            'pres_description': '',
            'pres_file': 'Upload Presentation File',
            'pres_image': 'Upload Presentation Cover',
            'pres_date': 'When are you going to Present? ',
            'stage': 'Choose a Stage',
            'type': 'Presentation Type',
        }
        widgets = {
            'pres_owner': forms.TextInput(
                attrs={"name": "owner", 'type': 'hidden', 'class': "form-control", 'placeholder': 'owner',
                       'id': 'presentation-owner'}),
            'pres_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': 'Presentation Name', 'id': 'presentation-name'}),
            'pres_description': forms.Textarea(
                attrs={'class': "form-control", 'placeholder': 'Presentation Description',
                       'id': 'presentation-description'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'pres_date': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Select a date',
                'type': 'date'
            }),

            'stage': forms.Select(attrs={'class': 'form-control'}),
            'pres_file': forms.ClearableFileInput(
                attrs={'class': "form-control", 'multiple': True, 'id': 'Presentation-file'}),
            'pres_image': forms.ClearableFileInput(
                attrs={'class': "form-control", 'multiple': True, 'id': 'Presentation-picture'}),
        }


class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        # questions = Criteria.objects.all()
        fields = ('criteria', 'evaluation',)

        labels = {
            'criteria': '',
            'evaluation': 'Rate 1-100'
        }
        widgets = {

            # 'criteria': forms.Select(attrs={'class': 'form-control'}),
            'evaluation': forms.NumberInput(
                attrs={"name": "evaluation", 'type': 'text', 'class': "form-control", 'placeholder': 'Rate',
                       'id': 'rate'}),
        }

class RevviewsForm(ModelForm):
    class Meta:
        model = Reviews
        # questions = Criteria.objects.all()
        fields = ('review1', 'review2','review3')

        labels = {
            'review1': 'How was the presentation 0-100',
            'review2': 'How was the project 0-100',
            'review3':'How was the style 0-100'
        }
        widgets = {

            # 'criteria': forms.Select(attrs={'class': 'form-control'}),
            'review1': forms.NumberInput(
                attrs={'type': 'number', 'class': "form-control", 'placeholder': 'Rate 0-100',
                       }),
            'review2': forms.NumberInput(
                attrs={'type': 'number', 'class': "form-control", 'placeholder': 'Rate 0-100',
                       }),
            'review3': forms.NumberInput(
                attrs={'type': 'number', 'class': "form-control", 'placeholder': 'Rate 0-100',
                       }),
        }