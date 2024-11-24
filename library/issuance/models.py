from django.contrib import messages
from django.db import models, transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from book_catalog.models import BookInstance, BookInstanceStatus
from users.models import User


class Issuance(models.Model):
    book_instance = models.ForeignKey(
        BookInstance, on_delete=models.CASCADE, verbose_name="ID экземпляра книги"
    )
    date_issue = models.DateTimeField(default=timezone.now, verbose_name="Дата выдачи")
    return_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата возврата",
    )
    reader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="issuance_reader",
        verbose_name="ID Читателя",
    )
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="issuance_employee",
        verbose_name="ID Сотрудника",
    )

    def save(self, *args, **kwargs):
        if not self.pk and self.book_instance.status.id != 1:
            raise ValueError("Книга не доступна для выдачи.")

        try:
            with transaction.atomic():
                if self.return_date:
                    new_status = get_object_or_404(BookInstanceStatus, id=1)
                else:
                    new_status = get_object_or_404(BookInstanceStatus, id=3)
                self.book_instance.status = new_status

                super().save(*args, **kwargs)
                self.book_instance.save()

        except Exception as e:
            request = kwargs.get("request")
            if request:
                messages.error(request, "Ошибка. Попробуйте позже.")
            raise

    class Meta:
        db_table = "issuance"
        verbose_name = "Выдачу книг"
        verbose_name_plural = "Выдача книг"
