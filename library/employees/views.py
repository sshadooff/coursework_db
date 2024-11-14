from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def employees(request):
    context = {
        "title": "Сотрудники",
        "content": "СПИСОК СОТРУДНИКОВ"
    }
    return render(request, "employees/employees.html", context)


def employee(request):
    context = {
        "title": "Информация о сотруднике",
        "content": "ИНФОРМАЦИЯ О СОТРУДНИКЕ"
    }
    return render(request, "employees/employee.html", context)