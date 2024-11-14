from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def readers(request):
    context = {
        "title": "Картотека",
        "content": "КАРТОТЕКА"
    }
    return render(request, "file_cabinet/readers.html", context)


def reader(request):
    context = {
        "title": "Информация о читателе",
        "content": "ИНФОРМАЦИЯ О ЧИТАТЕЛЕ"
    }
    return render(request, "file_cabinet/reader.html", context)