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

    context = {
        "book": book,
    }
    return render(request, "book_catalog/book.html", context)
