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
        'stripe_public_key': 'pk_test_51NxOH6IsJoMM7Nic9H1bA6RzNuMjNpEs4hD7fCY1RphEWQ890sxoVgCH3bcOESj6WDg2MTy4upRUftxdVr10ATh700VTClQWeI',
        'client_secret': 'test client secret',
    }

    return render(request, checkout_template, context)

