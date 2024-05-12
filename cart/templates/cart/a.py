ngo.shortcuts import redirect, render, reverse


def view_cart(request):
    """Add a quantity of the specified product to the shopping cart"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add quantity of specified plant to cart"""
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    if "plant_size" in request.POST:
        size = request.POST["plant_size"]
    cart = request.session.get("cart", {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]["items_by_size"].keys():
                cart[item_id]["items_by_size"][size] += quantity
            else:
                cart[item_id]["items_by_size"][size] = quantity
        else:
            cart[item_id] = {"items_by_size": {size: quantity}}
    else:

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session["cart"] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust teh quantity of the specified plant to the specified amount"""
    print('adjust', request)
    quantity = int(request.POST.get("quantity"))
    print('quantiyt', quantity)
    size = None
    if "plant_size" in request.POST:
        size = request.POST["plant_size"]
    cart = request.session.get("cart", {})

    if size:
        if quantity > 0:
            cart[item_id]["items_by_size"][size] = quantity
        else:
            del cart[item_id]["items_by_size"][size]
            if not cart[item_id]["items_by_size"]:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop[item_id]

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))

