from django.shortcuts import render
from .models import Restaurant


def home(request):
    restaurant = Restaurant.objects.first() # fetch the first restaurant
    context = {
        "restaurant_name": restaurant.name if restaurant else "Our Restaurant"
    }

    return render(request, "home.html", context)
