from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('plants'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51Of16vD1UHgIZx0CYc1lVjAdJPVYTbJcWVKMbi7Erxri5i9iyEDlTfUUGGlydDT08A3JwYUHArd11vcc7VjwGVdD00gUnB4OZm',
            'client_secret': 'test client secret',
            }

    return render(request, template, context)
