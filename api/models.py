from django.db import models


class Item(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='Product')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.IntegerField(default=0, verbose_name='Price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
