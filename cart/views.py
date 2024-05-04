from django.shortcuts import render, redirect


def view_cart(request):
    """Add a quantity of the specified product to the shopping cart"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add quantity of specified plant to cart"""
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get("cart", {})
    if str(item_id) in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session["cart"] = cart
    return redirect(redirect_url)
