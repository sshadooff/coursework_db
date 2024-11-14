from django.urls import path
from book_catalog import views

app_name = "book_catalog"

urlpatterns = [
    path("", views.books, name="index"),
    path("book/", views.book, name="book")
]
