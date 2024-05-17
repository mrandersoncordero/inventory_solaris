"""Product admin."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from .models import Category,  Product, Supplier

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""
    fieldsets = (
        ('Information', {
            'fields': ('name', 'description',),
        }),
    )
    
    list_display = ('pk', 'name', 'description')
    list_editable = ['name']
    search_fields = ('name', 'description')
