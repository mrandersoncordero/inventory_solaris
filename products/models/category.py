"""Category model."""

# Django
from django.db import models


# Utils
from inventory.utils import InformationBase


class Category(InformationBase):
    pass

    def __str__(self):
        return self.name