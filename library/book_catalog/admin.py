from django.contrib import admin

from book_catalog.models import (
    Author,
    Genre,
    Publisher,
    BookCatalog,
    BookInstance,
    BookInstanceStatus,
)


@admin.register(BookCatalog)
class BookCatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = [
        "id",
        "title",
        "author",
        "genre",
        "age_restriction",
        "copies_number",
    ]
    list_editable = ["copies_number"]
    search_fields = ["title"]
    list_filter = ["author", "genre", "age_restriction"]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("book",)}
    list_display = ["id", "book", "status", "publication_year", "publisher"]
    search_fields = ["publication_year"]
    list_filter = ["status", "publication_year", "publisher"]


@admin.register(BookInstanceStatus)
class BookInstanceStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "status"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "genre"]
    search_fields = ["genre"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ["id", "publisher"]
    search_fields = ["publisher"]
