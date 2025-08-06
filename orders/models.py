from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model): #store the menu of restaurant
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model): #Order model
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED','Canceled')

    ]

    customer = models.ForeignKey( #store the customer order
        User,
        on_delete = models.CASCADE,
        related_name = 'orders',
        verbose_name = 'Customer'
    )

    total_amount = models.DecimalField( #store total amount of order
        max_digits = 8,
        decimal_places = 2,
        verbose_name = 'Total Amount'
    )

    status = models.CharField( #store the status of oreder
        max_length = 10,
        choices = STATUS_CHOICES,
        default = 'PENDING',
        verbose_name = 'order status',

    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey( #links back to order 
        Order,
        on_delete = models.CASCADE,
        related_name = 'items'
    )

    menu_item = models.ForeignKey( # the dish being ordered
        Menu,
        on_delete = models.CASCADE, 
        related_name = 'order_item'
    )

    quantity = models.PositiveIntegerField(default=1) #how many items ordered

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}",

