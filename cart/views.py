from django.shortcuts import render, redirect

def view_cart(request):
    """A view that renders the cart contents pages"""

    return render(request, 'cart/cart.html')

def add_to_cart(reqeust, item_id):
    """Add quantity of specified plant to cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys());
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
