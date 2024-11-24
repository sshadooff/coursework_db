import re
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

    def clean_phone(self):
        data = self.cleaned_data["phone"]

        # Убираем пробелы и любые ненумерические символы
        data = re.sub(r"\s+", "", data)  # Убираем все пробелы
        data = re.sub(r"\D", "", data)  # Убираем все ненумерические символы

        # Проверяем, что номер телефона состоит из 11 цифр и начинается с '7' или '8'
        if len(data) != 11 or not (data.startswith("7") or data.startswith("8")):
            raise forms.ValidationError(
                "Номер телефона должен начинаться с 7 или 8 и состоять из 11 цифр."
            )

        return data


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
    phone = forms.CharField()

    def clean_phone(self):
        data = self.cleaned_data["phone"]

        # Убираем пробелы и любые ненумерические символы
        data = re.sub(r"\s+", "", data)  # Убираем все пробелы
        data = re.sub(r"\D", "", data)  # Убираем все ненумерические символы

        # Проверяем, что номер телефона состоит из 11 цифр и начинается с '7' или '8'
        if len(data) != 11 or not (data.startswith("7") or data.startswith("8")):
            raise forms.ValidationError(
                "Номер телефона должен начинаться с 7 или 8 и состоять из 11 цифр."
            )

        return data
