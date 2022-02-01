from django.urls import path
from .views import addtoshopcart, shopcard, deletefromcart, orderproduct


urlpatterns = [
    path('add_ticket_to_shop_card/<uuid:id>', addtoshopcart, name='add_ticket'),
    path('shop_card/', shopcard, name='shopcard'),
    path('shop_card/<int:id>', deletefromcart, name='delete_from_card'),
    path('order/', orderproduct, name='order'),
]