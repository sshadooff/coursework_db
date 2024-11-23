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
]
