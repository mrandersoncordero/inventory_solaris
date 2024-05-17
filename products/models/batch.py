"""Batch model."""

# Django
from django.db import models

# Models
from .product import Product

class Batch(models.Model):
    """Batch model."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batch_products')
    identifier = models.CharField(max_length=50) # Unique identifier for the batch
    production_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f"Batch {self.identifier} - {self.product.name}"
