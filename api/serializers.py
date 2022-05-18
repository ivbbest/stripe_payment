from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Стандартный сериализатор для сериализации данных
    """
    class Meta:
        model = Item
        fields = '__all__'
