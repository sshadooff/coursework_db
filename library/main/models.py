from django.db import models
from django.utils import timezone


class News(models.Model):
    heading = models.CharField(max_length=150, verbose_name="Заголовок")
    news = models.TextField(verbose_name="Новость")
    date_of_publication = models.DateField(
        default=timezone.localdate, verbose_name="Дата публикации"
    )

    class Meta:
        db_table = "news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.heading
