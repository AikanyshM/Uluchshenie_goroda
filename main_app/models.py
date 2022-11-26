from django.db import models
from account.models import User

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Название категории")
    text = models.TextField(verbose_name = "Описание категории")