from django.shortcuts import render
from .models import Laserapp


def index(request):
    products = Laserapp.objects.all()
    return render(request, 'index.html', {'products': products})
