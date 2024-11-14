from django.urls import path
from booking import views

app_name = "booking"

urlpatterns = [
    path("", views.booking, name="index"),
    path("one_booking/", views.one_booking, name="one_booking")
]
