from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'main_photo', 'date')

class Application(admin.ModelAdmin):
    list_display = ('name', 'description')
