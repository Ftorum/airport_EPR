from django.urls import path
from .views import FlightsView, TicketView, OrderView, OptionView, option_edit, OrderViewAll, status_edit, RoleView, role_edit, flight_edit, create_flight


urlpatterns = [
    path('', FlightsView.as_view(), name='index'),
    path('tickets/<uuid:id>', TicketView.as_view(), name='ticket'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('options/', OptionView.as_view(), name='options'),
    path('purchases/', OrderViewAll.as_view(), name='purchases'),
    path('employes/', RoleView.as_view(), name='employes'),
    path('edit_options/<int:id>', option_edit, name='edit_option'),
    path('edit_status/<int:id>', status_edit, name='edit_status'),
    path('edit_role/<int:id>', role_edit, name='edit_role'),
    path('edit_flight/<uuid:id>', flight_edit, name='edit_flight'),
    path('create_flight/', create_flight, name='create_flight'),
]