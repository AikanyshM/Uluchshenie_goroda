from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Житель')
    INN = models.PositiveSmallIntegerField(verbose_name = "ИНН", unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.user.first_name

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Мэрия')

    