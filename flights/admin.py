from django.contrib import admin
from .models import Flight, AirPlane, Ticket, Option

# Register your models here.
admin.site.register(Flight)
admin.site.register(AirPlane)
admin.site.register(Ticket)
admin.site.register(Option)