from orders.models import OrderItem, Order
from django.contrib import admin

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)