from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Reservations
from .forms import ReservationForm

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

@login_required
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # link reservation to logged-in user
            reservation.save()
            return redirect('reservations')  # change to your URL name
    else:
        form = ReservationForm()
    return render(request, 'restaurant/reservation_form.html', {'form': form})