from django.urls import path
from file_cabinet import views

app_name = "file_cabinet"

urlpatterns = [
    path("", views.readers, name="index"),
    path("reader/", views.reader, name="reader")
]
