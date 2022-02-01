from tkinter import CASCADE
from django.db import models
from sqlalchemy import null
from authy.models import Passenger
from django.forms import ModelForm
import uuid

# Create your models here.


class Ticket(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    flight_id = models.ForeignKey("Flight", on_delete=models.CASCADE)
    seats_number = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    

    def __str__(self):
        return str(self.flight_id)


class Option(models.Model):
    LUNCH_CHOICES = (
        ('None', 'None'),
        ('Fish', 'Fish'),
        ('Chicken', 'Chicken'),
        ('Pork', 'Pork'),
    )
    LUGGAGE_CHOICES = (
        ('None', 'None'),
        ('Small', 'Small'),
        ('Big', 'Big'),
        ('Extra Big', 'Extra Big'),
    )
    ticket_id = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    lunch = models.CharField(choices=LUNCH_CHOICES,
                             max_length=100, null=True, blank=True, default='None')
    luggage = models.CharField(
        choices=LUGGAGE_CHOICES, max_length=100, null=True, blank=True, default='None')

    def __str__(self):
        return str(self.ticket_id.flight_id) + ' ' + str(self.user_id.first_name)

class OptionForm(ModelForm):
    class Meta:
        model = Option
        fields = ['lunch','luggage']


class AirPlane(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Flight(models.Model):
    DEST_CHOICES = (
        ('New York to Washington DC', 'New York to Washington DC'),
        ('Washington DC to Miami', 'Washington DC to Miami'),
        ('Los Angeles to Dalas', 'Los Angeles to Dalas'),
    )
    GATE_CHOICES = (
        ('24F', '24F'),
        ('1A', '1A'),
        ('14D', '14D'),
        ('6B', '6B'),
    )
    STATUS_CHOICES = (
        ('Waiting for cheking-in', 'Waiting for cheking-in'),
        ('Check-in', 'Check-in'),
        ('Boarding', 'Boarding'),
        ('Boarding completed', 'Boarding completed'),
        ('Delayed', 'Delayed'),
        ('Canceled', 'Canceled'),
    )
    id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=101, null=True, blank=False)
    destinations = models.CharField(choices=DEST_CHOICES, max_length=100, blank=False)
    gate = models.CharField(choices=GATE_CHOICES, max_length=10, blank=True)
    flight_status = models.CharField(choices=STATUS_CHOICES, max_length=100, blank=False)
    date = models.DateField()
    airplane_id = models.ForeignKey(AirPlane, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.destinations)


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = ['number','destinations','gate','flight_status','date','airplane_id']

