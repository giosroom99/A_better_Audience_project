from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import *


class CreateStageForm(ModelForm):
    class Meta:
        model = Stage
        # Set the form fields
        fields = ('stage_name', 'category', 'stage_description', 'Stage_image',)

        labels = {
            'stage_name': '',
            'stage_description': '',
            'category': 'Select Stage Type',
            'Stage_image': ''
        }
        widgets = {

            'stage_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': 'Stage Name', 'id': 'stage-name'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Stage Type', }),
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
            'pres_file': 'Upload Presentation File (Only PDF Docs!)',
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
                attrs={'class': "form-control", 'multiple': True, 'accept': 'application/pdf'}),
            'pres_image': forms.ClearableFileInput(
                attrs={'class': "form-control", 'multiple': True, }),
        }


class approvalForm(ModelForm):
    class Meta:
        model = Presentation
        StageSelection = forms.ModelChoiceField(queryset=Stage.objects.all())
        # Set the form fields
        fields = (
            'approval',)
        labels = {
            'approval': 'Update Status',
        }
        widgets = {

            'approval': forms.Select(attrs={'class': 'form-control'}),

        }


class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ['answer', ]
        model = Answer

        widgets = {
            'answer': forms.NumberInput(
                attrs={'class': "form-control mb-3", 'placeholder': 'Rate 0-100', 'type': 'number'
                       }),
        }


class OpenEndedForm(forms.ModelForm):
    class Meta:
        fields = ['openEndedAnswer']
        model = OpenEndedAnswer

        widgets = {
            'openEndedAnswer': forms.TextInput(
                attrs={'class': "form-control mb-3", 'placeholder': 'Type here', 'type': 'text'
                       }),
        }


class BestPresentationForm(forms.ModelForm):
    class Meta:

        model = BestPresentation
        fields = ['rate', 'presentation']

        labels = {
            'presentation': 'Select your favorite Presentation',
            'rate':'Give your Favorite presentation a score (1-5)'
        }
        widgets = {
            'presentation': forms.Select(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(
                attrs={'class': "form-control mb-3", 'placeholder': 'Rate 1-5', 'type': 'number'
                       }),
        }
