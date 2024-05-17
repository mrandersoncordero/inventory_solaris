"""Inventory model."""

# Django
from django.db import models

# Utils
from administative_system.utils import BaseModel

# Models
from products.models import Product, Batch

class Inventory(BaseModel):
    """Inventory model."""

    name = models.CharField(max_length=100) # e.g, "Almacen Central"
    laction = models.CharField(max_length=100, blank=True, null=True)


class ProductInventory(BaseModel):
    """ProductInventory model."""
    
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE,
                                  related_name='intentories')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='products')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,
                              related_name='batchs')
    
    quantity = models.PositiveIntegerField(default=0)
    
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.inventory.name} - {self.product.name} - Batch: {self.batch.identifier} - Quantity: {self.quantity}"

