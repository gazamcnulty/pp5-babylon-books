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
from .forms import ProductForm, AuthorForm
from .models import Author , Book , Genre, Post #Review

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
    #reviews = book.review_set.all()
    #messages.success(request, f'You have added {book.title} to your bag')

    #if request.method == 'POST':
    #    review = Review.objects.create(
    #        user=request.user,
    #        book=book,
    #        text=request.POST.get('text')
    #    )
    #    return redirect('book_detail', book_id)


    context = {
        'book':book,
        'author':author,
    #    'reviews':reviews,
    }
    return render(request, 'book_detail.html', context)


@login_required(login_url='login')
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Changing store info is restricted to admin / superusers')
        return redirect(reverse('homepage'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required(login_url='login')
def add_author(request):
    if not request.user.is_superuser:
        messages.error(request, 'Changing store info is restricted to admin / superusers')
        return redirect(reverse('homepage'))
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added author!')
            return redirect(reverse('add_author'))
        else:
            messages.error(request, 'Failed to add author. Please ensure the form is valid.')
    else:
        form = AuthorForm()
    template = 'add_author.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required(login_url='login')
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Changing store info is restricted to admin / superusers')
        return redirect(reverse('homepage'))
    product = get_object_or_404(Book, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('book_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required(login_url='login')
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Changing store info is restricted to admin / superusers')
        return redirect(reverse('homepage'))
    product = get_object_or_404(Book, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('books'))



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

    book = Book.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f' {book.title} is in the bag')
    
    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):

    book = Book.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    context = {'book':book}
    request.session['bag'] = bag
    return redirect(reverse('bag'))


    
def remove(request, item_id):
    """Remove the item from the shopping bag"""

    book = Book.objects.get(id=item_id)
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
            messages.info(request, f'Removed {book.title} from bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing {book.title} from bag')
        return HttpResponse(status=500)


def blog(request):

    posts = Post.objects.all()

    paginator = Paginator(posts, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog.html', context)


def blog_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    #comments = post.comment_set.all()
    number_of_likes = post.number_of_likes()

    #if request.method == 'POST':
    #    comment = Comment.objects.create(
    #        user=request.user,
    #        post=post,
    #        text=request.POST.get('text')
    #    )
    #    return redirect('blog_detail.html', post_id)


    context = {
        'post': post,
        'number_of_likes': number_of_likes,
        #'comments': comments,
    }
    return render(request, 'blog_detail.html', context)



def post_like(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('blog_detail', post_id)