from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    """
    Добавление товаров для просмотра в админке сайта
    """
    list_display = ('name', 'description', 'price',)
    list_filter = ('price', 'name',)


admin.site.register(Item, ItemAdmin)
