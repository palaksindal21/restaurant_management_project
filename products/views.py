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


class MenuListView(APIView):
    # GET retrieve all menu items
    def get(self, request):
        # list of menu items
        menu_items = [
            {"name": "Margherita Pizza", "description": "Classic pizza with cheese and tomato sauce", "price": 250},
            {"name": "Veggie burger", "description": "Loaded with fresh veggies and cheese", "price": 180},
            {"name": "Pasta", "description": "Creamy alfredo sauce with mushrooms", "price": 300},
            {"name": "Cold coffee", "description": "Chilled coffee with ice cream", "price": 120}
            
        ]

        return Response(menu_items, status=status.HTTP_200_OK)


class CustomerListView(APIView):
    def get(self, request):
        try:
            customers = Customer.objects.all().order_by("-created_at")
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except DatabaseError as e:
            return Response(
                {"error":"A database error occured. Please try again later."},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
