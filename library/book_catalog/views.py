import csv
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from book_catalog.models import Author, BookCatalog, Genre


def books(request, page=1):
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

    paginator = Paginator(books, 6)
    current_page = paginator.page(page)

    context = {
        "title": "Книжный каталог",
        "content": "КНИЖНЫЙ КАТАЛОГ",
        "books": current_page,
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
    author = request.GET.get("author", None)
    genre = request.GET.get("genre", None)
    age_restriction = request.GET.get("age_restriction", None)

    books = BookCatalog.objects.all()

    if author:
        books = books.filter(author=author)

    if genre:
        books = books.filter(genre=genre)

    if age_restriction:
        books = books.filter(age_restriction=age_restriction)

    page_number = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 6)
    paginator = Paginator(books, page_size)

    try:
        page = paginator.page(page_number)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    books_list = list(
        page.object_list.values(
            "title", "author", "genre", "age_restriction", "annotation"
        )
    )

    return JsonResponse(books_list, safe=False)


def export_books_to_csv(request):
    author = request.GET.get("author", None)
    genre = request.GET.get("genre", None)
    age_restriction = request.GET.get("age_restriction", None)

    books = BookCatalog.objects.all()

    if author:
        books = books.filter(author=author)

    if genre:
        books = books.filter(genre=genre)

    if age_restriction:
        books = books.filter(age_restriction=age_restriction)

    page_number = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 6)
    paginator = Paginator(books, page_size)

    try:
        page = paginator.page(page_number)
    except Exception as e:
        return HttpResponse(f"Ошибка страницы: {str(e)}", status=400)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(["title", "author", "genre", "age_restriction", "annotation"])

    for book in page.object_list:
        writer.writerow(
            [book.title, book.author, book.genre, book.age_restriction, book.annotation]
        )

    return response
