# Generated by Django 3.2 on 2022-11-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
                ('text', models.TextField(verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Краткое название')),
                ('description', models.TextField(verbose_name='Описание новости')),
                ('main_photo', models.ImageField(upload_to='news_main_image', verbose_name='Фото новости')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата новости')),
            ],
        ),
    ]
