from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Reservations

# Create your views here.

def home(request):
  return render(request, 'restaurant/home.html')

def menu(request):
  return render(request, 'restaurant/menu.html')

class ReservationsList(LoginRequiredMixin, generic.ListView):
    """
    This will only display the reservations of the logged in user
    """
    
    template_name = 'reservations/reservations_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        # Filter reservations by logged-in user
        return Reservations.objects.filter(user=self.request.user).order_by('-date', '-time')