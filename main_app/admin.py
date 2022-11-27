from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'main_photo', 'date')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'application_photo', 'date', 'location', 'user', 'category')
