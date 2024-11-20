from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения"
    )
    phone = models.CharField(
        max_length=12, unique=True, blank=True, null=True, verbose_name="Номер телефона"
    )

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
