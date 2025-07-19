from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservations(models.Model):
    # ForeignKey - username from User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Name on the reservation
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    # Reservation details
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1)

    # Notes for allergens and others
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # To show the reservation on the admin
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} at {self.time}"