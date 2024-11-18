# Generated by Django 4.2.16 on 2024-11-17 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Автора',
                'verbose_name_plural': 'Авторы',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20, unique=True, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'genre',
            },
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_catalog.bookcatalog', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='bookcatalog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_catalog.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='bookcatalog',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_catalog.genre', verbose_name='Жанр'),
        ),
    ]