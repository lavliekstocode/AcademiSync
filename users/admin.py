from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'school', 'resume')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

