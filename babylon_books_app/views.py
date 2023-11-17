from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView
from . import views 
from .models import Author , Book , Genre

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
    genres = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                books = books.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

        if 'genre' in request.GET:
            genres = request.GET['genre'].split()
            books = books.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)


    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'current_genre':genres,
        'current_sorting': current_sorting,
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
        return render(request, 'search_results.html',
                      {'search_response': search_response,
                       'books':books})
    else:
        return render(request, 'search_results.html',
                      {'search_response': search_response}
                      )


def about(request):
    return render(request, 'about.html')


def bag(request):
    return render(request, 'bag.html')


def add_to_bag(request, item_id):


    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):


    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    
    request.session['bag'] = bag
    return redirect(reverse('bag'))


    
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

