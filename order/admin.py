from django.contrib import admin
from .models import ShopCard, Order, OrderProduct

# Register your models here.
admin.site.register(ShopCard)
admin.site.register(Order)
admin.site.register(OrderProduct)