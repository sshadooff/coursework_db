import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from book_catalog.models import Author, BookCatalog, Genre


def books(request):
    books = BookCatalog.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    age_restrictions = {book.age_restriction for book in books}

    author = request.GET.get("author", None)
    genre = request.GET.get("genre", None)
    age_restriction = request.GET.get("age_restriction", None)

    if author:
        books = books.filter(author=author)

    if genre:
        books = books.filter(genre=genre)

    if age_restriction:
        books = books.filter(age_restriction=age_restriction)

    context = {
        "title": "Книжный каталог",
        "content": "КНИЖНЫЙ КАТАЛОГ",
        "books": books,
        "authors": authors,
        "genres": genres,
        "age_restrictions": age_restrictions,
    }
    return render(request, "book_catalog/books.html", context)


def book(request, book_slug):

    book = BookCatalog.objects.get(slug=book_slug)
    title = book.title

    context = {
        "title": title,
        "book": book,
    }
    return render(request, "book_catalog/book.html", context)


def export_books_to_json(request):
    books = BookCatalog.objects.all()

    books_list = list(
        books.values("title", "author", "genre", "age_restriction", "annotation")
    )

    return JsonResponse(books_list, safe=False)


def export_books_to_csv(request):
    books = BookCatalog.objects.all()

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(["title", "author", "genre", "age_restriction", "annotation"])

    for book in books:
        writer.writerow(
            [book.title, book.author, book.genre, book.age_restriction, book.annotation]
        )

    return response
