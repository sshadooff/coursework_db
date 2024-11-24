from django.urls import path
from issuance import views

app_name = "issuance"

urlpatterns = [
    path("", views.issuance, name="index"),
]
