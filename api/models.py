from django.db import models


class Item(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
