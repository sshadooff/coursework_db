from django.shortcuts import render

from book_catalog.models import BookInstance


def booking(request):
    context = {
        "title": "Бронирование",
        "content": "ЗАБРОНИРОВАННЫЕ КНИГИ"
    }
    return render(request, "booking/booking.html", context)


def select_book_instance(request, book_id):
    book_instances = BookInstance.objects.filter(book_id=book_id)

    context = {
        "title": "Выбор экземпляра книги",
        "content": "ВЫБЕРИТЕ ЭКЗЕМПЛЯР КНИГИ",
        "book_instances": book_instances
    }
    return render(request, "booking/select_book_instance.html", context)