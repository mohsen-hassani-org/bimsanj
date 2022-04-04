from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('mobile', 'username', 'first_name', 'last_name', 'is_staff', 'email')
    search_fields = ('mobile', 'username', 'first_name', 'last_name', 'email', 'notes')
    fieldsets = (
        (None, {'fields': ('mobile', 'username', 'password')}),
        ('اطلاعات فردی', {'fields': ('first_name', 'last_name', 'email')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ("تاریخ‌های مهم", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'username', 'password1', 'password2')}
         ),
    )
