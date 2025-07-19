from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'restaurant/home.html')

def menu(request):
  return render(request, 'restaurant/menu.html')