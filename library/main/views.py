from django.shortcuts import render


def index(request):
    context = {"title": "Главная", "content": "ДОБРО ПОЖАЛОВАТЬ!"}
    return render(request, "main/index.html", context)
