from django.contrib import admin

from main.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "heading",
        "news",
        "date_of_publication",
    ]
    search_fields = ["id", "heading"]
