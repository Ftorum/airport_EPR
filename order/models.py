from ast import Pass
from django.db import models
from sqlalchemy import SmallInteger
from authy.models import Passenger
from flights.models import Ticket


from django.forms import ModelForm

# Create your models here.
class ShopCard(models.Model):
    user_id = models.ForeignKey(Passenger, on_delete=models.SET_NULL, null=True)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user_id.first_name

    @property
    def price(self):
        return (self.ticket_id.price)

    @property
    def amount(self):
        return (self.quantity * self.ticket_id.price)



class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCard
        fields = ['quantity']


class Order(models.Model):
    user = models.ForeignKey(Passenger, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    credit_card = models.CharField(blank=True, max_length=20)
    code = models.CharField(max_length=5, editable=False )
    total = models.FloatField()
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
        

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','phone','credit_card']

class OrderProduct(models.Model):
    TICKET_CHOICES = (('None', 'None'),('Registred', 'Registred'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=TICKET_CHOICES, max_length=100, blank=True, default='None')

    def __str__(self):
        return self.ticket.flight_id.number

class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['status']


