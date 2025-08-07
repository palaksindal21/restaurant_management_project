from django.contrib import admin
from .models import Menu, Order, OrderItem #importing models

@admin.register(Menu) #register the menu model using custom class
class MenuAdmin(admin.ModelAdmin):
    #fields to display in admin view
    list_display = ('name', 'price')

    #enable search functionality for these fields
    search_fields = ('name','price')

    #add filtering options based on price
    list_filter = ('price',)

class OrderItemInline(admin.TabularInline): #define an inline admin class to allow editing order item within the order admin
    model = OrderItem #specify which model to use inline
    extra = 1 #show extra row after adding

#register order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    #field to display in admin list view
    list_display = ('id', 'customer', 'status', 'total_amount', 'created_at')

    #enable filteing options for creation date and status
    list_filter = ('status', 'created_at')

    #allow searching by customer's name
    search_fields = ('customer__username',)

    #diplay orederitem inline within order edit page
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    #fields to show in list view
    list_display = ('order', 'menu_item', 'quantity')

    #enable search by menu item name and customer name
    search_fields = ('menu_item__name', 'order__customer__username')


