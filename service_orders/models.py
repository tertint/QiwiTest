from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Order(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.CharField(max_length=55)

    def __str__(self):
        return f'Id {self.id}: {self.description}'
