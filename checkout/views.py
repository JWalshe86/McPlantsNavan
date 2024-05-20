from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('plants'))
    
    current_cart = cart_contents(request)
    total = current_cart['grand_total']    
    stripe_total = round(total * 100 )

    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51Of16vD1UHgIZx0CYc1lVjAdJPVYTbJcWVKMbi7Erxri5i9iyEDlTfUUGGlydDT08A3JwYUHArd11vcc7VjwGVdD00gUnB4OZm',
            'client_secret': 'test client secret',
            }

    return render(request, template, context)
