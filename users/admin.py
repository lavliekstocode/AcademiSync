from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Document

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'school', 'resume')}),
    )
    list_display = ('username', 'email', 'role', 'school')
    list_filter = ('role',)
    search_fields = ('username', 'email')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Document, DocumentAdmin)
