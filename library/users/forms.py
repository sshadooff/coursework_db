from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "date_of_birth",
            "email",
            "phone",
            "password1",
            "password2",
        ]

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "date_of_birth",
            "email",
            "phone",
        ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    date_of_birth = forms.CharField()
    email = forms.CharField()
