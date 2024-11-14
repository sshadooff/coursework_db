from django.urls import path
from employees import views

app_name = "employees"

urlpatterns = [
    path("", views.employees, name="index"),
    path("employee/", views.employee, name="employee")
]
