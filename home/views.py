from django.shortcuts import render


def home(request):
    restaurant = Restaurant.objects.first()
    context = {
        "restaurant_name": restaurant.name if restaurant else "My restaurant",
        "phone_number": restaurant.phone if restaurant else "N/A",
    }
    return render(request, "home.html", context)
