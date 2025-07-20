from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reservations
from .forms import ReservationForm

def home(request):
    return render(request, 'restaurant/home.html')

def menu(request):
    return render(request, 'restaurant/menu.html')

class ReservationsList(LoginRequiredMixin, generic.ListView):
    """
    View to display the reservations to logged in user
    """

    template_name = 'reservations/reservations_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        # Filter reservations by logged-in user
        return Reservations.objects.filter(user=self.request.user).order_by('-date', '-time')

class ReservationCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new reservation.

    It will redirect to the new reservation page

    After creating the new reservation it will
    redirect to the reservations page
    """

    model = Reservations
    form_class = ReservationForm
    template_name = 'restaurant/reservation_form.html'
    success_url = reverse_lazy('reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to edit a reservation.

    Displays a pre-filled form with the reservation details 
    allowing the logged in user to make changes.

    After updating redirects to the reservations page.
    """

    model = Reservations
    form_class = ReservationForm
    template_name = 'restaurant/reservation_form.html'
    success_url = reverse_lazy('reservations')

    def get_queryset(self):
        return Reservations.objects.filter(user=self.request.user)

class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete a reservation.

    The logged in user is able to delete a reservation.

    After deleting redirects to reservations.
    """

    model = Reservations
    template_name = 'restaurant/reservation_confirm_delete.html'
    success_url = reverse_lazy('reservations')

    def get_queryset(self):
        return Reservations.objects.filter(user=self.request.user)
