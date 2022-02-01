from django.shortcuts import render
from flights.models import Ticket, Option
from authy.models import Passenger
from .models import ShopCartForm, ShopCard, OrderForm, OrderProduct, Order
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



@login_required
def addtoshopcart(request,id):
    user = request.user.id
    ticket = Ticket.objects.get(id=id)
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            data = ShopCard()
            data.user_id = Passenger.objects.get(user=user)
            data.ticket_id = ticket
            data.quantity = form.cleaned_data['quantity']
            data.save()
            messages.success(request, "Ticket added to Shopcart ")
            return HttpResponseRedirect(url)
    else:
        form = ShopCartForm()

    return render(request, 'ticket_form.html', {'form': form, 'ticket': ticket})


@login_required
def shopcard(request):
    current_user = request.user  # Access User Session information
    shopcard = ShopCard.objects.filter(user_id=Passenger.objects.get(user=current_user))
    total=0
    for rs in shopcard:
        total += rs.ticket_id.price * rs.quantity
    #return HttpResponse(str(total))
    context={'shopcard': shopcard,
             'total': total,
             }
    return render(request,'shopcard.html',context)


def deletefromcart(request,id):
    ShopCard.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect("/shop_card")


@login_required
def orderproduct(request):
    current_user = request.user
    shopcard = ShopCard.objects.filter(user_id=Passenger.objects.get(user=current_user))
    total = 0
    for rs in shopcard:
        total += rs.ticket_id.price * rs.quantity
    if request.method == 'POST':  
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            user_buing = Passenger.objects.get(user=current_user)
            data.user = user_buing
            data.first_name = form.cleaned_data.get('first_name')
            data.last_name = form.cleaned_data.get('last_name')
            data.phone = form.cleaned_data.get('phone')
            data.credit_card = form.cleaned_data.get('credit_card')
            data.total = total
            ordercode= get_random_string(5).upper() 
            data.code =  ordercode
            data.save()
            send_mail(
                'Booking info',
                'Your ticket:  {0}\Total pay: {1}\n'.format(ordercode, total),
                'lacky3462@yandex.ru',
                [user_buing.user.email],
                fail_silently=False,
            ) 

            for rs in shopcard:
                detail = OrderProduct()
                detail.order_id     = data.id # Order Id
                detail.ticket   = rs.ticket_id
                detail.user      = Passenger.objects.get(user=current_user)
                detail.quantity     = rs.quantity
                detail.price    = rs.price
                detail.amount        = rs.amount
                detail.save()
                # ***Reduce quantity of sold product from Amount of Product
                ticket = Ticket.objects.get(id=rs.ticket_id.id)
                ticket.seats_number -= rs.quantity
                ticket.save()
                #************ <> *****************
                option = Option.objects.create(ticket_id=ticket, user_id=Passenger.objects.get(user=current_user))

            ShopCard.objects.filter(user_id=Passenger.objects.get(user=current_user)).delete() # Clear & Delete shopcart
            messages.success(request, "Your Order has been completed. Thank you ")
            return render(request, 'shopcard.html', {'ordercode':ordercode})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    form= OrderForm()
    profile = Passenger.objects.get(user=current_user)
    context = {'shopcard': shopcard,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'order.html', context)