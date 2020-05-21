from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):  # signup form
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.CharField(max_length=254, help_text='Required. Inform a valid email address')
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=60)

    class Meta:
        model = User  # predefined user model
        fields = ('username', 'password', 'email')  # {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}
