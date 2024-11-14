from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def personal_account(request):
    context = {
        "title": "Личный кабинет",
        "content": "ЛИЧНЫЙ КАБИНЕТ"
    }
    return render(request, "personal_account/personal_account.html", context)