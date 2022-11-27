from django.contrib import admin
from .models import User, Citizen, AdminUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email', 'first_name', 'last_name')

class CitizenAdmin(admin.ModelAdmin):
    list_display = ('user', 'id',  'INN')

class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(User, UserAdmin)
admin.site.register(Citizen, CitizenAdmin)
admin.site.register(AdminUser, AdminUserAdmin)