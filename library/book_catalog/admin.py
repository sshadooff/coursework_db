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


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("book",)}


admin.site.register(BookInstanceStatus)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
