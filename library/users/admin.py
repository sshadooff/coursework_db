from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "date_of_birth",
        "email",
        "phone",
    ]
    search_fields = ["username", "first_name", "last_name", "email", "phone"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.is_staff:
            qs = qs.filter(is_staff=False)
        return qs
