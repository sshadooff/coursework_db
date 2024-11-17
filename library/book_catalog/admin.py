from django.contrib import admin

from book_catalog.models import BookCatalog, BookInstance, BookInstanceStatus

admin.site.register(BookCatalog)
admin.site.register(BookInstance)
admin.site.register(BookInstanceStatus)
