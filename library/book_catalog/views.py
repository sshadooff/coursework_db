from django.shortcuts import render

from book_catalog.models import BookCatalog


def books(request):
    books = BookCatalog.objects.all()

    context = {
        "title": "Книжный каталог",
        "content": "КНИЖНЫЙ КАТАЛОГ",
        "books": books,
    }
    return render(request, "book_catalog/books.html", context)


def book(request, book_slug):

    book = BookCatalog.objects.get(slug=book_slug)

    context = {
        "book": book,
    }
    return render(request, "book_catalog/book.html", context)
