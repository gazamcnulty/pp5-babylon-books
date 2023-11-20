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

