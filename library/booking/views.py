from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

from book_catalog.models import BookInstance, BookInstanceStatus
from booking.models import Booking


def booking(request):
    now = timezone.now()

    active_bookings = Booking.objects.filter(
        booking_end_date__gte=now, reader=request.user
    )

    past_bookings = Booking.objects.filter(
        booking_end_date__lt=now, reader=request.user
    )

    context = {
        "title": "Бронирование",
        "content1": "АКТИВНЫЕ БРОНИРОВАНИЯ",
        "content2": "ИСТОРИЯ БРОНИРОВАНИЙ",
        "active_bookings": active_bookings,
        "past_bookings": past_bookings,
    }
    return render(request, "booking/booking.html", context)


def select_book_instance(request, book_id):
    book_instances = BookInstance.objects.filter(book_id=book_id, status="1")

    context = {
        "title": "Выбор экземпляра книги",
        "content": "ВЫБЕРИТЕ ЭКЗЕМПЛЯР КНИГИ",
        "book_instances": book_instances,
    }
    return render(request, "booking/select_book_instance.html", context)


def book_book_instance(request, book_instance_id):
    book_instance = get_object_or_404(BookInstance, id=book_instance_id)

    if book_instance.status.id == 1:
        try:
            with transaction.atomic():
                Booking.objects.create(book_instance=book_instance, reader=request.user)
                new_status = get_object_or_404(BookInstanceStatus, id=2)
                book_instance.status = new_status
                book_instance.save()

            messages.success(
                request,
                f"{request.user}, Вы успешно забронировали книгу {book_instance.book.title}.",
            )
            return redirect("booking:index")
        except Exception as e:
            messages.error(request, f"Ошибка: {str(e)}. Попробуйте позже.")
            return redirect("book_catalog:index")


def cancel_book_book_instance(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    book_instance = booking.book_instance

    try:
        with transaction.atomic():
            booking.booking_end_date = timezone.now()
            booking.save()
            book_instance.status = BookInstanceStatus.objects.get(id=1)
            book_instance.save()

        messages.success(request, f"{request.user}, Ваше бронирование отменено.")
        return redirect("booking:index")

    except Exception as e:
        messages.error(
            request, f"Ошибка при отмене бронирования: {str(e)}. Попробуйте позже."
        )
        return redirect("booking:index")
