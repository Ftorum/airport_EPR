from re import template
from ssl import Options
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Flight, Ticket, Option, OptionForm, FlightForm
from order.models import OrderProduct, OrderForm, OrderProductForm
from authy.models import Passenger, PassangerForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class FlightsView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['flights'] = Flight.objects.all()
        return context

class TicketView(LoginRequiredMixin,TemplateView):
    template_name = 'ticket.html'

    def get_context_data(self, id, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tickets'] = Ticket.objects.filter(flight_id=id)
        return context

class OptionView(TemplateView):
    template_name = 'options.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['options'] = Option.objects.all()
        return context

class OrderView(LoginRequiredMixin, TemplateView):
    template_name = 'booked_flights.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['orders'] = OrderProduct.objects.filter(user=Passenger.objects.get(user=self.request.user))
        return context

class OrderViewAll(LoginRequiredMixin, TemplateView):
    template_name = 'all_purchases.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['orders'] = OrderProduct.objects.all()
        return context

class RoleView(LoginRequiredMixin, TemplateView):
    template_name = 'roles.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['employes'] = Passenger.objects.all()
        return context

def option_edit(request, id):
    option = Option.objects.get(id = id)
    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            option.lunch = form.cleaned_data.get('lunch')
            option.luggage = form.cleaned_data.get('luggage')
            option.save()
            return HttpResponseRedirect(reverse('options'))
    else:
        form = OptionForm()
    context = {
    'form': form,
    'option': option,
    }
    return render(request, 'option_form.html', context)


def status_edit(request, id):
    order = OrderProduct.objects.get(id = id)
    if request.method == 'POST':
        form = OrderProductForm(request.POST)
        if form.is_valid():
            order.status = form.cleaned_data.get('status')
            order.save()
            return HttpResponseRedirect(reverse('purchases'))
    else:
        form = OrderProductForm()
    context = {
    'form': form,
    'order': order,
    }
    return render(request, 'purchase_form.html', context)

def role_edit(request, id):
    passanger = Passenger.objects.get(id = id)
    if request.method == 'POST':
        form = PassangerForm(request.POST)
        if form.is_valid():
            passanger.role = form.cleaned_data.get('role')
            passanger.save()
            return HttpResponseRedirect(reverse('employes'))
    else:
        form = PassangerForm()
    context = {
    'form': form,
    'passanger': passanger,
    }
    return render(request, 'roles_edit.html', context)

def flight_edit(request, id):
    flight = Flight.objects.get(id = id)
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight.number = form.cleaned_data.get('number')
            flight.destinations = form.cleaned_data.get('destinations')
            flight.gate = form.cleaned_data.get('gate')
            flight.flight_status = form.cleaned_data.get('flight_status')
            flight.date = form.cleaned_data.get('date')
            flight.airplane_id = form.cleaned_data.get('airplane_id')
            flight.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FlightForm()
    context = {
    'form': form,
    'flight': flight,
    }
    return render(request, 'flight_edit.html', context)

def create_flight(request):
    flight = Flight()
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight.number = form.cleaned_data.get('number')
            flight.destinations = form.cleaned_data.get('destinations')
            flight.gate = form.cleaned_data.get('gate')
            flight.flight_status = form.cleaned_data.get('flight_status')
            flight.date = form.cleaned_data.get('date')
            flight.airplane_id = form.cleaned_data.get('airplane_id')
            flight.save()
            tickets_create =Ticket(flight_id=flight, seats_number=299, price=30)
            tickets_create.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FlightForm()
    context = {
    'form': form,
    'flight': flight,
    }
    return render(request, 'flight_create.html', context)