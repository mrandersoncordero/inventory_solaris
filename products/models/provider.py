"""Provider model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utils
from inventory.utils import InventorySolaris

class Provider(InventorySolaris, models.Model):
    """Provider model."""

    name = models.CharField(max_length=100)
    
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="El número de teléfono debe introducirse en el formato: +9999999. Hasta 15 dígitos permitidos"
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
    