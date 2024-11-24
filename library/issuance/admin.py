from django.contrib import admin
from book_catalog.models import BookInstance
from issuance.models import Issuance
from users.models import User


@admin.register(Issuance)
class IssuanceAdmin(admin.ModelAdmin):
    readonly_fields = ["employee"]
    list_display = [
        "id",
        "book_instance",
        "date_issue",
        "return_date",
        "reader",
        "employee",
    ]
    search_fields = ["id"]
    list_filter = ["book_instance", "reader", "employee"]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "book_instance":
            if request.resolver_match.kwargs.get("object_id"):
                kwargs["queryset"] = BookInstance.objects.all()
            else:
                kwargs["queryset"] = BookInstance.objects.filter(status__id=1)

        if db_field.name == "reader":
            kwargs["queryset"] = User.objects.filter(is_staff=False)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.employee = request.user
        else:
            if obj.return_date:
                obj.employee = request.user

        obj.save()
