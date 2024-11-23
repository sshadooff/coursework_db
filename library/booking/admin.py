from django.contrib import admin

from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "book_instance",
        "booking_start_date",
        "booking_end_date",
        "reader",
    ]
    search_fields = ["id"]
    list_filter = ["book_instance", "reader"]
