from django.shortcuts import render
from django.views import generic
from .models import Reservations

# Create your views here.

def home(request):
  return render(request, 'restaurant/home.html')

def menu(request):
  return render(request, 'restaurant/menu.html')

class ReservationsList(generic.ListView):
    queryset = Reservations.objects.all()
    template_name = 'reservations/reservations_list.html'
    context_object_name = 'reservations'