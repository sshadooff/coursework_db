from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Имя")
    last_name = models.CharField(max_length=128, verbose_name="Фамилия")

    class Meta:
        db_table = "author"
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    genre = models.CharField(max_length=20, unique=True, verbose_name="Жанр")

    class Meta:
        db_table = "genre"
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


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


class BookInstanceStatus(models.Model):
    status = models.CharField(max_length=20, unique=True, verbose_name="Статус")

    class Meta:
        db_table = "book_instance_status"
        verbose_name = "Статус экземпляра книги"
        verbose_name_plural = "Статусы экземпляров книг"


class BookInstance(models.Model):
    book = models.ForeignKey(
        BookCatalog, on_delete=models.CASCADE, verbose_name="Книга"
    )
    status = models.ForeignKey(
        BookInstanceStatus, on_delete=models.CASCADE, verbose_name="Статус"
    )
    publication_year = models.SmallIntegerField(verbose_name="Год публикации")

    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "book_instance"
        verbose_name = "Экземпляр книги"
        verbose_name_plural = "Экземпляры книг"
