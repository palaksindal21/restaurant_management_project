from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MenuItem(serializers.Modelserializer):   #MenuItem serializer
    class Meta:
        model = Menu
        fields = '__all__'
