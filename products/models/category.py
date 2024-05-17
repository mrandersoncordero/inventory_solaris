"""Category model."""

# Django
from django.db import models

class Category(models.Model):
    """Category model."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name