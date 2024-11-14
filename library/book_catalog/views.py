from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def books(request):
    context = {
        "title": "Книжный каталог",
        "content": "КНИЖНЫЙ КАТАЛОГ"
    }
    return render(request, "book_catalog/books.html", context)


def book(request):
    context = {
        "title": "Информация о книге",
        "content": "ИНФОРМАЦИЯ О КНИГЕ"
    }
    return render(request, "book_catalog/book.html", context)