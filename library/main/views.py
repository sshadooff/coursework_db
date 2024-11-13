from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {
        'title': 'Главная',
        'content': 'ДОБРО ПОЖАЛОВАТЬ!'
    }
    return render(request, "main/index.html", context)
