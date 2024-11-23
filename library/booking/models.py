from django.db import models
from datetime import timedelta

from django.utils import timezone

from book_catalog.models import BookInstance
from users.models import User


class Booking(models.Model):
    book_instance = models.ForeignKey(
        BookInstance, on_delete=models.CASCADE, verbose_name="ID экземпляра книги"
    )
    booking_start_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата начала бронирования"
    )
    booking_end_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата окончания бронирования",
    )
    reader = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="ID Читателя"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.booking_end_date:
            self.booking_end_date = self.booking_start_date + timedelta(days=7)
            self.save(update_fields=["booking_end_date"])

    class Meta:
        db_table = "booking"
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
