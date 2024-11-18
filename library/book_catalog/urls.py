from django.urls import path
from book_catalog import views

app_name = "book_catalog"

urlpatterns = [
    path("", views.books, name="index"),
    path("book/<slug:book_slug>", views.book, name="book"),
]
