from django.db import models
from account.models import User

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Название категории")
    text = models.TextField(verbose_name = "Описание категории")

class News(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Краткое название')
    description = models.TextField(verbose_name='Описание новости')
    main_photo = models.ImageField(verbose_name=('Фото новости'), upload_to='news_main_image')
    date = models.DateField(auto_now_add=True, verbose_name= 'Дата новости')
