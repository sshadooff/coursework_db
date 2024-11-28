from django.db import models
from django.db import transaction
from datetime import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Имя")
    last_name = models.CharField(max_length=128, verbose_name="Фамилия")

    class Meta:
        db_table = "author"
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    genre = models.CharField(max_length=20, unique=True, verbose_name="Жанр")

    class Meta:
        db_table = "genre"
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre


class BookCatalog(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    age_restriction = models.IntegerField(verbose_name="Возрастное ограничение")
    copies_number = models.IntegerField(verbose_name="Количество экземпляров")
    annotation = models.TextField(blank=True, null=True, verbose_name="Аннотация")
    image = models.ImageField(
        upload_to="book_image", blank=True, null=True, verbose_name="Изображение"
    )

    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "book_catalog"
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"
        ordering = ["id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.copies_number > 0:
            current_year = datetime.now().year
            with transaction.atomic():
                for i in range(self.copies_number):
                    instance_slug = f"{self.slug}-{i + 1}"
                    BookInstance.objects.create(
                        book=self,
                        status=BookInstanceStatus.objects.first(),
                        publication_year=current_year,
                        slug=instance_slug,
                    )


class BookInstanceStatus(models.Model):
    status = models.CharField(max_length=20, unique=True, verbose_name="Статус")

    class Meta:
        db_table = "book_instance_status"
        verbose_name = "Статус экземпляра книги"
        verbose_name_plural = "Статусы экземпляров книг"

    def __str__(self):
        return self.status


class Publisher(models.Model):
    publisher = models.CharField(
        max_length=20, unique=True, verbose_name="Издательство"
    )

    class Meta:
        db_table = "publisher"
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self):
        return self.publisher


class BookInstance(models.Model):
    book = models.ForeignKey(
        BookCatalog, on_delete=models.CASCADE, verbose_name="Книга"
    )
    status = models.ForeignKey(
        BookInstanceStatus, on_delete=models.CASCADE, verbose_name="Статус"
    )
    publication_year = models.SmallIntegerField(verbose_name="Год публикации")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, default=1, verbose_name="Издательство"
    )

    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "book_instance"
        verbose_name = "Экземпляр книги"
        verbose_name_plural = "Экземпляры книг"

    def __str__(self):
        return f"Экземпляр книги: {self.book.title}, ID: {self.id}"
