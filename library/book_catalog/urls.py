from django.urls import path
from book_catalog import views

app_name = "book_catalog"

urlpatterns = [
    path("", views.books, name="index"),
    path("book/<slug:book_slug>", views.book, name="book"),
    path("export/json/", views.export_books_to_json, name="export_books_to_json"),
    path("export/csv/", views.export_books_to_csv, name="export_books_to_csv"),
]
