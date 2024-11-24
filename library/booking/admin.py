from django.contrib import admin
from book_catalog.models import BookInstance
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "book_instance":
            if request.resolver_match.kwargs.get("object_id"):
                kwargs["queryset"] = BookInstance.objects.all()
            else:
                kwargs["queryset"] = BookInstance.objects.filter(status__id=1)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
