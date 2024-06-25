from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ChoiceForm(forms.Form):
    CHOICES = [
        ('token', 'токенизация'),
        ('lem', 'лемматизация'),
        ('stem', 'стемминг'),
    ]
    CHOICES_LANG = [
        ('en', 'en'),
        ('rus', 'rus'),
    ]
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    choice_lang = forms.ChoiceField(choices=CHOICES_LANG, widget=forms.RadioSelect)
    text = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 200,
        'rows': 3,
        'style': 'width: 100%',
    }))

