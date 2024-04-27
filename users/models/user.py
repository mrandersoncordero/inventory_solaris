"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from inventory.utils import InventorySolaris

class User(InventorySolaris, AbstractUser):
    """User model.

    Extend form Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={'unique': 'A user with that email already exists.'}
    )

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self) -> str:
        """Return username"""
        return self.username

    def get_short_name(self) -> str:
        """Return username."""
        return self.username
