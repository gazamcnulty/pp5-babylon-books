from django.shortcuts import render
from . import views

# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def books(request):
    return render(request, 'books.html')
