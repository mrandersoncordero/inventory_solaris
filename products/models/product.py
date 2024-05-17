"""Product model."""

# Django
from django.db import models

# Models
from .category import Category
from .supplier import Supplier

# Utils
from administative_system.utils import BaseModel


class Product(BaseModel, models.Model):
    """Product model."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_stock = models.PositiveIntegerField(default=0)
    max_stock = models.PositiveIntegerField(default=0)
    unit_measure = models.CharField(max_length=50, default='unit')
    wight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='categories')

    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, blank=True, null=True,
                                 related_name='suppliers')

    def __str__(self):
        return self.name
    