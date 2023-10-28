from django.shortcuts import render
from . import views

# Create your views here.


def index(request):
    return render(request, 'babylon_books_app/index.html')
