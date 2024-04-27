"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# Models
from .models.user import User

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 
                'is_staff',
                'groups', 
                'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff'),
        }),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(User, UserAdmin)