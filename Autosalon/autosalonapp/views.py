
from django.shortcuts import render
from .models import Brand, Car

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def filiallar(request):
    return render(request, 'filiallar.html')
