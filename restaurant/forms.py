from allauth.account.forms import SignupForm
from django import forms
from .models import Reservations


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30,
                                 label="First Name",
                                 required=True)
    last_name = forms.CharField(max_length=30,
                                label="Last Name",
                                required=True)

    field_order = [
        "first_name",
        "last_name",
        "username",
        "email",
        "password1",
        "password2",
    ]

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ["first_name",
                  "last_name",
                  "date",
                  "time",
                  "guests",
                  "message"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date",
                                           "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time",
                                           "class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "guests": forms.NumberInput(attrs={"class": "form-control",
                                               "min": 1}),
            "message": forms.Textarea(attrs={"class": "form-control",
                                             "rows": 3}),
        }
