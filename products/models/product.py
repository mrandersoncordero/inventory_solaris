"""Product model."""

# Django
from django.db import models

# Models
from .category import Category
from .fabrict import Fabrict
from .provider import Provider

# Utils
from inventory.utils import InventorySolaris


class Product(InventorySolaris, models.Model):
    """Product model."""

    SIZE = {
        'S': 'S',
        'M': 'M',
        'L': 'L',
        'XL': 'XL',
        'XXL': 'XXL',
        'XXXL': 'XXXL'
    }

    GENDER = {
        'M': 'Maculino',
        'F': 'Femenino'
    }

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=50)
    size = models.CharField(
        max_length=4, 
        choices=SIZE, 
        default=SIZE['S']
    )
    gender = models.CharField(
        max_length=1, 
        choices=GENDER, 
        default=GENDER['M']
    )

    fabric = models.ForeignKey(Fabrict, 
                               on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, 
                                 on_delete=models.RESTRICT)
    provider = models.ForeignKey(Provider, 
                                 on_delete=models.RESTRICT)

    quantity = models.BigIntegerField()
    unit_price = models.FloatField()

    price_sale_dolar = models.FloatField()
    price_sale_bs = models.FloatField()

    def __str__(self):
        return self.name
    