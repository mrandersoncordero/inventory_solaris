"""Supplier model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utils
from administative_system.utils import BaseModel

class Supplier(BaseModel, models.Model):
    """Supplier model."""


    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="El número de teléfono debe introducirse en el formato: +9999999. Hasta 20 dígitos permitidos"
    )

    contact = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[phone_regex], max_length=20)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.contact}"
    