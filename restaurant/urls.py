from django.urls import path
from .views import (
    home,
    menu,
    ReservationsList,
    ReservationCreateView,
    ReservationUpdateView,
    ReservationDeleteView,
)

urlpatterns = [
    path('', home, name='restaurant-home'),
    path('menu/', menu, name='menu'),
    path('reservations/', ReservationsList.as_view(), name='reservations'),
    path('reservations/new/', ReservationCreateView.as_view(), name='reservation_create'),
    path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
]