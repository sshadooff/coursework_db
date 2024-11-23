from django.urls import path
from booking import views

app_name = "booking"

urlpatterns = [
    path("", views.booking, name="index"),
    path(
        "select-book-instance/<int:book_id>",
        views.select_book_instance,
        name="select_book_instance",
    ),
    path(
        "book-book-instance/<int:book_instance_id>",
        views.book_book_instance,
        name="book_book_instance",
    ),
    path(
        "cancel-book-book-instance/<int:booking_id>",
        views.cancel_book_book_instance,
        name="cancel_book_book_instance",
    ),
]
