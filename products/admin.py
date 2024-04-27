"""Product admin."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from .models import Category, Fabrict, Product, Provider

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


@admin.register(Fabrict)
class FabrictAdmin(admin.ModelAdmin):
    """Fabrict admin."""
    fieldsets = (
        ('Information', {
            'fields': ('name', 'description',),
        }),
    )
    
    list_display = ('pk', 'name', 'description')
    list_editable = ['name']
    search_fields = ('name', 'description')


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    """Provider admin."""
    fieldsets = (
        ('Information', {
            'fields': ('name', 'phone_number', 'email', 'address'),
        }),
        ('Metadata', {
            'fields': ('created', 'updated'),
        }),
    )
    
    list_display = ('pk', 'name', 'phone_number', 'email', 'address')
    list_editable = ['name', 'phone_number', 'email']
    search_fields = ('name', 'email')

    readonly_fields = ('created', 'updated')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin."""
    fieldsets = (
        (None, {
            'fields': (
                ('code', 'name'),
                ('description'),
                ('color', 'size', 'gender'),
                ('fabric', 'category', 'provider'),
                ('quantity')
            ),
        }),
        ('Precios', {
            'fields': (
                'unit_price', 
                'price_sale_dolar',
                'price_sale_bs',
            ),
        }),
        ('Metadata', {
            'fields': ('created', 'updated'),
        }),
    )

    list_display = (
        'code', 
        'name', 
        'color', 
        'size', 
        'gender', 
        'fabric', 
        'category', 
        'provider', 
        'unit_price', 
        'price_sale_dolar', 
        'price_sale_bs'
    )
    list_display_links = ['code']

    list_editable = [
        'name',
        'color',
        'size',
        'gender',
        'unit_price', 
        'price_sale_dolar',
    ]

    search_fields = [
        'name',
        'color',
        'size',
        'gender__name',
        'category__name',
        'fabric__name',
    ]

    list_filter = [
        'name',
        'color',
        'size',
        'category__name',
        'fabric__name',
        'created',
        'updated',
    ]
    readonly_fields = ('created', 'updated')

    