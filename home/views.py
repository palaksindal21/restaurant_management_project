from django.shortcuts import render
from .models import Restaurant


def home(request):
    restaurant = Restaurant.objects.first() # fetch the first restaurant
    context = {
        "restaurant_name": restaurant.name if restaurant else "Our Restaurant"
    }

    return render(request, "home.html", context)


def about(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    context = {
        "restaurant_name": restaurant_name,
        "description": "We server delicious food from fresh ingredients, offering a variety of dishes to satisfy every taste.",
        "image_url": "static/images/restaurant.jpg"
    }

    return render(request, "about.html", context)