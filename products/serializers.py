from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MenuItem(serializers.Modelserializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
