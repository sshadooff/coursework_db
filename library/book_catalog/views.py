from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from book_catalog.models import BookCatalog


def books(request):
    books = BookCatalog.objects.all()

    context = {
        "title": "Книжный каталог",
        "content": "КНИЖНЫЙ КАТАЛОГ",
        "books": books,
    }
    return render(request, "book_catalog/books.html", context)


def book(request):
    context = {
        "title": "Информация о книге",
        "content": "ИНФОРМАЦИЯ О КНИГЕ"
    }
    return render(request, "book_catalog/book.html", context)