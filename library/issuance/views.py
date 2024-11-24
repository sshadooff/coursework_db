from django.shortcuts import render

from issuance.models import Issuance


def issuance(request):
    active_issuances = Issuance.objects.filter(
        return_date__isnull=True, reader=request.user
    )

    past_issuances = Issuance.objects.filter(
        return_date__isnull=False, reader=request.user
    )

    context = {
        "title": "Выдача",
        "content1": "ВЫДАННЫЕ КНИГИ",
        "content2": "ВОЗВРАЩЕННЫЕ КНИГИ",
        "active_issuances": active_issuances,
        "past_issuances": past_issuances,
    }
    return render(request, "issuance/issuance.html", context)
