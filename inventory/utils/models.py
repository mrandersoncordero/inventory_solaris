"""Django models utilities."""

# Django
from django.db import models

class InventorySolaris(models.Model):
    """InventorySolaris base model.
      + created (DateTime): Store the datetime the objects was created.
      + modified (DateTime): Store the datetime the objects was modified
    """

    created = models.DateTimeField(
        'created',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    updated = models.DateTimeField(
        'updated',
        auto_now=True,
        help_text='Date time on which the object was last updated'
    )

    class Meta:
        """Meta options."""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-updated']


class InformationBase(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True