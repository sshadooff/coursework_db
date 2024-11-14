from django.urls import path
from personal_account import views

app_name = "personal_account"

urlpatterns = [
    path("", views.personal_account, name="index"),
]
