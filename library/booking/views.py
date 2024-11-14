from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def booking(request):
    context = {
        "title": "Бронирование",
        "content": "ЗАБРОНИРОВАННЫЕ КНИГИ"
    }
    return render(request, "booking/booking.html", context)


def one_booking(request):
    context = {
        "title": "Информация о бронировании",
        "content": "ИНФОРМАЦИЯ О БРОНИРОВАНИИ"
    }
    return render(request, "booking/one_booking.html", context)