from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .models import Menu
from .serializers import MenuItemSerializer
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuView(APIView): 
    # GET - retrieve all menu
    def get(self, request):
        menu_item = Menu.objects.all() # fetch all menu items from database
        serializer = MenuItemSerializer(menu_item, many=True)
        return response(serializer.data, status=status.HTTP_200_OK)

    # POST add a new menu item
    def post(self, request):
        serializer = MenuItemSerializer(data=request.data) # Take JSON from request
        if serializer.is_valid(): # validate incoming data
            serializer.save() # save item to database
            return response(serializer.data, status=status.HTTP_201_CREATED)
        return response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
