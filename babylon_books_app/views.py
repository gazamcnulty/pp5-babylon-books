from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView
from . import views 
from .models import Author , Book

# Create your views here.


def homepage(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors,
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')


def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    author = Author.objects.all()

    context = {
        'book':book,
        'author':author,
    }
    return render(request, 'book_detail.html', context)



def search_results(request):
    if request.method == "POST":
        search_response = request.POST['search_response']
        books = Book.objects.filter(
            title__icontains=search_response)
        authors = Author.objects.filter(
            name__icontains=search_response)
        return render(request, 'search_results.html',
                      {'search_response': search_response,
                       'books':books, 'authors':authors})
    else:
        return render(request, 'search_results.html',
                      {'search_response': search_response}
                      )


def about(request):
    return render(request, 'about.html')
