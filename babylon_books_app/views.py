from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from . import views 
from .models import Author , Book

# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')


def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context)


def about(request):
    return render(request, 'about.html')
