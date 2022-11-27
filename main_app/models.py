from tabnanny import verbose
from django.db import models
from account.models import User

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Название категории")
    text = models.TextField(verbose_name = "Описание категории")

    def __str__(self):
        return self.title
class News(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Краткое название')
    description = models.TextField(verbose_name='Описание новости')
    main_photo = models.ImageField(verbose_name=('Фото новости'), upload_to='news_main_image')
    date = models.DateField(auto_now_add=True, verbose_name= 'Дата новости')

    def __str__(self):
        return self.name

class Application(models.Model):
    title = models.CharField(max_length=150, verbose_name = "Заголовок заявки")
    text = models.TextField(verbose_name="Описание заявки")
    application_photo = models.ImageField(verbose_name='Фото', upload_to='application_image')
    date = models.DateField(auto_now_add=True, verbose_name= 'Дата заявки')
    location = models.CharField(max_length=150, verbose_name="Адрес происшествия")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Выберете категорию')

    def __str__(self):
        return self.title