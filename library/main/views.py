from django.shortcuts import render

from main.models import News


def index(request):
    quote = "Книга – одно из самых великих изобретений человеческого ума – обогащает опытом нашу жизнь. Какое же счастье для человека, что ему дана возможность дружить с книгой и пользоваться её неиссякаемой мудростью. А. Горбатов"

    news = News.objects.all()

    context = {
        "title": "Главная",
        "content1": "ДОБРО ПОЖАЛОВАТЬ!",
        "quote": quote,
        "content2": "НОВОСТИ",
        "news": news,
    }
    return render(request, "main/index.html", context)
