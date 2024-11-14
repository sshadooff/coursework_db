from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def issuance(request):
    context = {
        "title": "Выдача",
        "content": "ВЫДАННЫЕ КНИГИ"
    }
    return render(request, "issuance/issuance.html", context)


def issue(request):
    context = {
        "title": "Информация о выдаче",
        "content": "ИНФОРМАЦИЯ О ВЫДАЧЕ"
    }
    return render(request, "issuance/issue.html", context)