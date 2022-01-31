from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.CharField(
        max_length=200, required=True, widget=forms.EmailInput(), help_text='fill the email ')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
