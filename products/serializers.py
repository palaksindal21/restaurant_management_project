from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MenuItem(serializers.ModelSerializer):   # MenuItem serializer
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'description']
