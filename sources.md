







#SOURCES

For the process of completing this project, I followed along with the Boutique Ado tutorials. This was necessary for the E-commerce parts of the project and related apps. It mainly comprises the content of 

- checkout app , models, views, templates
- profiles app, models, views, templates
- allauth set up
- snippets.js
- readme.md
- includes / toasts


I am aware it is standard process to follow along with the tutorials as part of the project and its to be expected that the CI code would be included in the project , but I wanted to as thorough and comprehensive as possible when listing any and all sources. Below I have copied as many of the code snippets I was able to note from the Boutique Ado tutorial which were used in the creation of the Babylon Books project. The code below was instructed as part of the Boutique Ado tutorials and used in my own project, it may vary slightly due to different model names etc. The full Boutique Ado repo can be found here,  [Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546 )

  there are also links below to the progressive completion of the Boutique Ado repo, when it was not completed and had different content.




Filter items from data models

The guide in the tutorial Queries and Categories Part 1 and 2 is useful for this, I used it in my project


def books(request):
    books = Book.objects.all()
    genres = None

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split()
            books = books.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    context = {
        'books': books,
        'current_genre':genres,
    }
    return render(request, 'books.html', context)


<ul class="dropdown-menu">
              <li><a class="dropdown-item" href="{% url 'books' %}">All</a></li>
              <li><a class="dropdown-item" href="{% url 'books' %}?genre=Classics">Classics</a></li>
              <li><a class="dropdown-item" href="{% url 'books' %}?genre=Horror" >Horror</a></li>
              <li><a class="dropdown-item" href="{% url 'books' %}?genre=Scifi" >Scifi</a></li>
              <li><a class="dropdown-item" href="{% url 'books' %}?genre=Fantasy" >Fantasy</a></li>
            </ul>





github link 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/673a36fdd4bb2c09f8843c6ad8cb6ae4a60dda01/templates/includes/main-nav.html )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/673a36fdd4bb2c09f8843c6ad8cb6ae4a60dda01/templates/includes/main-nav.html


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)





** ________________________________________




** filter data / objects within the <a> link itself

I got this from the tutorial Sorting Products Part 2 , github link 
[Link]( https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/ec933ec96eeb42b40e0534e40d40fb38cc999940/products/templates/products/products.html )
 https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/ec933ec96eeb42b40e0534e40d40fb38cc999940/products/templates/products/products.html

 <a class="text-muted" href="{% url 'products' %}?category={{ product.category.name }}">


I use this in my own code to filter the books by genre, you can click the listed genre in any book to be brought to the genre page 
books.html
 <a href="{% url 'books' %}?genre={{ book.genre.name }}"><p>{{ book.genre }}</p></a>




**___________________________


I followed along for the set up of cart / add to cart from the tutorials - The Shopping Bag

github
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/9c2aa64f4edffb25e330d722ee66542e553edb80 )
 https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/9c2aa64f4edffb25e330d722ee66542e553edb80

**contexts.py 


def cart_items(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    for book_id, quantity in cart.books():
        product = get_object_or_404(Book, id=book_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'book_id':book_id,
            'quantity':quantity,
            'product': product,
        })
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context


**____________________________________


Add to cart form , from tutorials
Git hub 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/21e3b111100f5c8daa4bc6e9565bde09980b33d8/products/templates/products/product_detail.html )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/21e3b111100f5c8daa4bc6e9565bde09980b33d8/products/templates/products/product_detail.html


** form in product details

  <form class="form" action="{% url 'add_to_cart' book.id %}" method="POST">
            {% csrf_token %}
            <div class="form-row">
                <div class="col-12">
                    <p class="mt-3"><strong>Quantity:</strong></p>
                    <div class="form-group w-50">
                        <div class="input-group">
                            <input class="form-control qty_input" type="number" name="quantity" value="1" min="1" max="99" data-item_id="{{ book.id }}" id="id_qty_{{ book.id }}">
                        </div>
                    </div>
                </div>
                <div class="col-12">
                    <a href="{% url 'books' %}" class="btn btn-outline-black rounded-0 mt-5">
                        <span class="icon">
                            <i class="fas fa-chevron-left"></i>
                        </span>
                        <span class="text-uppercase">Keep Shopping</span>
                    </a>
                    <input type="submit" class="btn btn-black rounded-0 text-uppercase mt-5" value="Add to Bag">
                </div>
                <input type="hidden" name="redirect_url" value="{{ request.path }}">
            </div>
        </form>


** view


def add_to_cart(request, book_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    if book_id in list(cart.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag




** grand total in cart 


<p class="my-0">
                                    {% if grand_total %}
                                        ${{ grand_total|floatformat:2 }}
                                    {% else %}
                                        $0.00
                                    {% endif %}
                                </p>



**_________________________________________

 + - quantity buttons for add to cart , in book_detail.html

Taken from tutorials , Adding Products Part 5 
Git Hub
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/0a5335f2e95f58b10207ea57cedcdd063251a3ff/products/templates/products/product_detail.html )
 https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/0a5335f2e95f58b10207ea57cedcdd063251a3ff/products/templates/products/product_detail.html




 <div class="input-group">
                            <div class="input-group-prepend">
                                <button class="decrement-qty btn btn-black rounded-0" 
                                    data-item_id="{{ book.id }}" id="decrement-qty_{{ book.id }}">
                                    <span class="icon">
                                        <i class="fas fa-minus"></i>
                                    </span>
                                </button>
                            </div>
                            <input class="form-control qty_input" type="number" name="quantity" value="1" min="1" max="99" data-item_id="{{ book.id }}" id="id_qty_{{ book.id }}">
                            <div class="input-group-append">
                                <button class="increment-qty btn btn-black rounded-0"
                                    data-item_id="{{ book.id }}" id="increment-qty_{{ book.id }}">
                                    <span class="icon">
                                        <i class="fas fa-plus"></i>
                                    </span>
                                </button>
                            </div>
                        </div>



 javascript for quantity / includes page
 [Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/0a5335f2e95f58b10207ea57cedcdd063251a3ff/products/templates/products/includes/quantity_input_script.html )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/0a5335f2e95f58b10207ea57cedcdd063251a3ff/products/templates/products/includes/quantity_input_script.html



<script type="text/javascript">

    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue - 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });
</script>





**________________________


 method of updating / removing items from cart , anchor elements working with javascript


[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/7e5faf3f2fc5fe20e382f91ea0b86a28b4917359/bag/templates/bag/bag.html )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/7e5faf3f2fc5fe20e382f91ea0b86a28b4917359/bag/templates/bag/bag.html



 <a class="update-link text-info"><small>Update</small></a>
                        <a class="remove-item text-danger float-right" id="remove_{{ item.item_id }}" data-size="{{ item.size }}"><small>Remove</small></a>



 - -- - - 

{% block postloadjs %}
{{ block.super }}
{% include 'products/includes/quantity_input_script.html' %}
<script type="text/javascript">
    // Update quantity on click
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })
    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var size = $(this).data('size');
        var url = `/bag/remove/${itemId}`;
        var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};
        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })
</script>




**____________________________________

Adjust cart view to remove items 



def adjust_cart(request, book_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[book_id] = quantity
    else:
        cart.pop[book_id] = quantity
    
    request.session['cart'] = cart
    return redirect(reverse('cart'))






** __________________________________________



followed along with tutorial in method of how to add toasts when adding to bag / removing etc
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/e5323862cc7563f65526f0108f37c57ad92f7931 )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/e5323862cc7563f65526f0108f37c57ad92f7931


updated views to show message when item is added


else:
        bag[item_id] = quantity
        messages.success(request, f' {book.title} added to your bag')

postload js in base.html

    {% block postloadjs %}
    <script type="text/javascript">
        $('.toast').toast('show';)
    </script> 
    {% endblock %}






**------------------------------------------

CHECKOUT APP

 creating checkout and stripe payment 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/8486523459273dddf96932a4ae19dd9a83af679d/checkout/templates/checkout/checkout.html )

https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/8486523459273dddf96932a4ae19dd9a83af679d/checkout/templates/checkout/checkout.html




CHECKOUT MODELS


import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from babylon_books_app.models import Book

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.CASCADE)
    #product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.book.price * self.quantity
        super().save(*args, **kwargs)
    def __str__(self):
        return f'SKU {self.book.sku} on order {self.order.order_number}'






CHECKOUT URLS

from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout')
]


CHECKOUT VIEWS





from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from . import models

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('books'))
    order_form = OrderForm()
    checkout_template = 'checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, checkout_template, context)















FORMS.PY

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False



CHECKOUT - FORM - TEMPLATE


                <form action="{% url 'checkout' %}" method="POST" id="payment-form">
                    {% csrf_token %}
                    <fieldset class="rounded px-3 mb-5">
                        <legend class="fieldset-label small text-black px-2 w-auto">Details</legend>
                        {{ order_form.full_name | as_crispy_field }}
                        {{ order_form.email | as_crispy_field }}
                    </fieldset>
                    <fieldset class="rounded px-3 mb-5">
                        <legend class="fieldset-label small text-black px-2 w-auto">Delivery</legend>
                        {{ order_form.phone_number | as_crispy_field }}
                        {{ order_form.country | as_crispy_field }}
                        {{ order_form.postcode | as_crispy_field }}
                        {{ order_form.town_or_city | as_crispy_field }}
                        {{ order_form.street_address1 | as_crispy_field }}
                        {{ order_form.street_address2 | as_crispy_field }}
                        {{ order_form.county | as_crispy_field }}
                        <div class="form-check form-check-inline float-right mr-0">
							{% if user.is_authenticated %}
								<label class="form-check-label" for="id-save-info">Save this delivery information to my profile</label>
                                <input class="form-check-input ml-2 mr-0" type="checkbox" id="id-save-info" name="save-info" checked>
							{% else %}
								<label class="form-check-label" for="id-save-info">
                                    <a class="text-info" href="{% url 'account_signup' %}">Create an account</a> or 
                                    <a class="text-info" href="{% url 'account_login' %}">login</a> to save this information
                                </label>
							{% endif %}
						</div>
                    </fieldset>
                    <fieldset class="px-3">
                        <legend class="fieldset-label small text-black px-2 w-auto">Payment</legend>
                        <!-- A Stripe card element will go here -->
                        <div class="mb-3" id="card-element"></div>

                        <!-- Used to display form errors -->
                        <div class="mb-3 text-danger" id="card-errors" role="alert"></div>
                    </fieldset>

                    <div class="submit-button text-right mt-5 mb-2">                    
						<a href="{% url 'view_bag' %}" class="btn btn-outline-black rounded-0">
							<span class="icon">
								<i class="fas fa-chevron-left"></i>
							</span>
							<span class="font-weight-bold">Adjust Bag</span>
						</a>
						<button id="submit-button" class="btn btn-black rounded-0">
							<span class="font-weight-bold">Complete Order</span>
							<span class="icon">
								<i class="fas fa-lock"></i>
							</span>
						</button>
						<p class="small text-danger my-0">
							<span class="icon">
								<i class="fas fa-exclamation-circle"></i>
							</span>
							<span>Your card will be charged <strong>${{ grand_total|floatformat:2 }}</strong></span>
						</p>
					</div>
                </form>





**----------------------------------------------------------------------------------------------------------------------------------------

STRIPE 

**---------------------------------------------------------------------------------------------------------------------------------


Followed along with the stripe tutorial
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/6b3837fb56fdb60655292badbb2dcf649a074ec7/checkout/static/checkout/js/stripe_elements.js )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/6b3837fb56fdb60655292badbb2dcf649a074ec7/checkout/static/checkout/js/stripe_elements.js





/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/






STRIPE_ELEMENTS.JS  ---------------------------------------------------

 from tutorial , mostly uses stipe documentation 



/*
    Core logic/payment flow for this comes from here:
    [Link](https://stripe.com/docs/payments/accept-a-payment )
    https://stripe.com/docs/payments/accept-a-payment

*/
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');
// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
// Handle form submit
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});




** CHECKOUT SUCCESS ------------------------------------------------------


[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/4f4a39d898c2c347e0d0a0201e4c0d2d6ef1c500/checkout/templates/checkout/checkout_success.html )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/4f4a39d898c2c347e0d0a0201e4c0d2d6ef1c500/checkout/templates/checkout/checkout_success.html



Followed along closely with tutorial info , cycling through template language order fields to show info 


<div class="col-12 mt-5">
            <h2 class="text-center mt-5">Your purchase is complete, thank you!</h2>
            <p>Order confirmation will be sent to {{ order.email }}</p>
            <div class="row mt-5">
                <div class="col mx-auto">
                    <h5>Order Info</h5>
                    <p>Order Number : {{ order.order_number }}</p>
                    <p>Order Date : {{ order.date }}</p>
                </div>
                <div class="col mx-auto">
                    <h5>Order Info</h5>
                    {% for item in order.lineitems.all %}
                        <p>{{ item.product.name }}</p>
                        <p>{{ item.quantity }} @ ${{ item.product.price }} each</p>
                    {% endfor %}
                </div>
                <div class="col mx-auto">
                    <h5>Delivery Info</h5>
                    <p>Orderer : {{ order.full_name }}</p>
                    <p>Telephone number : {{ order.phone_number }}</p>
                    <p>Delivery address : {{ order.street_address1 }} <br>
                        {% if order.street_address2 %} {{ order.street_address1 }} {% endif %} <br>
                        {% if order.county %} {{ order.county }} {% endif %} <br>
                        {{ order.town_or_city }} <br>
                        {% if order.postcode %} {{ order.postcode }} {% endif %} <br>
                        {{ order.country }}
                        </p>
                </div>
                <div class="col mx-auto">
                    <h5>Billing info</h5>
                    <p>Delivery Cost : {{ order.delivery_cost }}</p>
                    <p>Total Cost : {{ order.grand_total }}</p>
                </div>
            </div>




** CHECKOUT LOADING OVERLAY ----------------------------------------------------
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/4f4a39d898c2c347e0d0a0201e4c0d2d6ef1c500/checkout/static/checkout/css )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/4f4a39d898c2c347e0d0a0201e4c0d2d6ef1c500/checkout/static/checkout/css




<div id="loading-overlay">
                <h1 class="text-light logo-font loading-spinner">
                    <span class="icon">
                        <i class="fas fa-3x fa-sync-alt fa-spin"></i>
                    </span>
                </h1>
            </div>



Css

#loading-overlay {
	display: none;
	position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(23, 162, 184, .85);
    z-index: 9999;
}

.loading-spinner {
	display: flex;
    align-items: center;
    justify-content: center;
    margin: 0;
    height: 100%;
}




** checkout/views.py 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/be009dd6c8db8c9cbc18aa5b8dd8a04daa194ed0/checkout/views.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/be009dd6c8db8c9cbc18aa5b8dd8a04daa194ed0/checkout/views.py


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            #commented out below, while receiving error 'NoneType' object has no attribute 'split'.
            #Error page says its related to checkout/views.py line 52 : pid = request.POST.get('client_secret').split('_secret')[0] 
            #I will return to this if I can get it working
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            #order = order_form.save()
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Book.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Book.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('books'))
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
    
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    if 'bag' in request.session:
        del request.session['bag']
    template = 'checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)











*WEBHOOKS  ----------------------------------------------------------------------------------
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/6502c7d3ec6465c89aef07ce8437ed36f4d43aa7/checkout/webhook_handler.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/6502c7d3ec6465c89aef07ce8437ed36f4d43aa7/checkout/webhook_handler.py


 webhooks_handler.py from tutorials



Webhook_handler.py ---------------------





from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
import json
import time
class StripeWH_Handler:
    """Handle Stripe webhooks"""
    def __init__(self, request):
        self.request = request
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated
        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)




Webhooks.py ----------------------------
From stripe documentation + tutorial 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/cdf3e76a67d03b6ed0e59d903869f04a0e1c4bb5/checkout/webhooks.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/cdf3e76a67d03b6ed0e59d903869f04a0e1c4bb5/checkout/webhooks.py



from django.http import HttpResponse
from .models import Order, OrderLineItem
from babylon_books_app.models import Book
import json
import time
class StripeWH_Handler:
    """Handle Stripe webhooks"""
    def __init__(self, request):
        self.request = request
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated
        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()      
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

** stripe elements js 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/06d30a8846a2867503bff714f796830caf46c3a0/checkout/static/checkout/js/stripe_elements.js )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/06d30a8846a2867503bff714f796830caf46c3a0/checkout/static/checkout/js/stripe_elements.js


/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');
// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
// Handle form submit
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});


** def cache_checkout_data to check if 'save info' option is ticked  ------------------------
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/06d30a8846a2867503bff714f796830caf46c3a0/checkout/views.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/06d30a8846a2867503bff714f796830caf46c3a0/checkout/views.py


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


Url for cache_checkout_data  

path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),

**---PROFILES ----------------------------------------------------------
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/95864bc75ef940aa002976163d7885612c6ca04b/profiles/models.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/95864bc75ef940aa002976163d7885612c6ca04b/profiles/models.py

Copied along with tutorial in creating UserProfile model 



from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


Views.py 


from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)





** forms.py ----------------------------------------------

For user profile form in profile.html , copied from tutorial






from django import forms
from .models import UserProfile
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/149abda4318106704ac8d3118b8e5a63ef070619/profiles/forms.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/149abda4318106704ac8d3118b8e5a63ef070619/profiles/forms.py

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


**profile.html -----------------------------------

 from tutorial 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/be009dd6c8db8c9cbc18aa5b8dd8a04daa194ed0/profiles/templates/profiles/profile.html )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/be009dd6c8db8c9cbc18aa5b8dd8a04daa194ed0/profiles/templates/profiles/profile.html






<h4>Profile Info</h4>
                <div class="col mx-auto">
                    <form class="" action="{% url 'profile' %}" method="POST" id="profile-update-form">
                        {% csrf_token %}
                        {{ form|crispy }}
                        <button>Update</button>
                    </form>
                </div>




{% for order in orders %}

                                        <a href="{% url 'order_history' order.order_number %}"
                                        title="{{ order.order_number }}">
                                            {{ order.order_number|truncatechars:6 }}
                                        </a>

                                   <p>{{ order.date }}</p>
                                        <ul class="list-unstyled">
                                            {% for item in order.lineitems.all %}
                                                <li class="small">
                                                    {% if item.product.has_sizes %}
                                                        Size {{ item.product.size|upper }}
                                                    {% endif %}{{ item.product.name }} x{{ item.quantity }}
                                                </li>
                                            {% endfor %}
                                        </ul>
                                   <p>${{ order.grand_total }}</p>
                                </tr>
                            {% endfor %}




** order history -------------------------------------------



In views.py , order_history view


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


** confirmation emails  ---------------------------------------------------------------------------------------






** ADD PRODUCTS ===============================================


 from tutorial , slight changes for my own model names / 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/90bfac3ad4932550b4457a698f7df8ab79a681bc/products/views.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/90bfac3ad4932550b4457a698f7df8ab79a681bc/products/views.py


**Forms.py-----------------------------------


from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'



**add_product.html ----------------------------------------


{% block content %}
    <div class="overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6">
                <hr>
                <h2 class="logo-font mb-4">Product Management</h2>
                <h5 class="text-muted">Add a Product</h5>
                <hr>
            </div>
        </div>

        <div class="row">
            <div class="col-12 col-md-6">
                <form method="POST" action="{% url 'add_product' %}" class="form mb-2" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form | crispy }}
                    <div class="text-right">
                        <a class="btn btn-outline-black rounded-0" href="{% url 'products' %}">Cancel</a>
                        <button class="btn btn-black rounded-0" type="submit">Add Product</button>
                    </div>
                </form>
            </div>            
        </div>
    </div>
{% endblock %}



**add_product view


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




**delete_product view



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



** Image field  / widgets.py ---------------------------------------------------------------------
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/bef1c8f38ea2774f75b18c15d5927b5409083cf9/products/widgets.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/bef1c8f38ea2774f75b18c15d5927b5409083cf9/products/widgets.py



from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'

** custom_clearable_file_input.html -------------------



{% if widget.is_initial %}
    <p>{{ widget.initial_text }}:</p>
    <a href="{{ widget.value.url }}">
        <img width="96" height="96" class="rounded shadow-sm" src="{{ widget.value.url }}">
    </a>
    {% if not widget.required %}
        <div class="custom-control custom-checkbox mt-2">
            <input class="custom-control-input" type="checkbox" name="{{ widget.checkbox_name }}" id="{{ widget.checkbox_id }}">
            <label class="custom-control-label text-danger" for="{{ widget.checkbox_id }}">{{ widget.clear_checkbox_label }}</label>
        </div>
    {% endif %}<br>
    {{ widget.input_text }}
{% endif %}
<span class="btn btn-black rounded-0 btn-file">
    Select Image <input id="new-image" type="{{ widget.type }}" name="{{ widget.name }}"{% include "django/forms/widgets/attrs.html" %}>
</span>
<strong><p class="text-danger" id="filename"></p></strong>




** EMAILS ----------------------



In settings.py 
[Link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/a07c1ca5a3b973eb47e5c944829cea06ead3936d/boutique_ado/settings.py )
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/a07c1ca5a3b973eb47e5c944829cea06ead3936d/boutique_ado/settings.py


if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'babylonbooks@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

** NOT WORKING


**404 
[Link](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/0713d55c023943438d418d83caf4171b/ )


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)



