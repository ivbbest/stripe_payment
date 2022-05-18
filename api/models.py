from django.db import models


class Item(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
