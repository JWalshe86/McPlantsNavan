from django.shortcuts import redirect, render, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from plants.models import Plant

def view_cart(request):
    """A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add quantity of specified plant to cart"""

    plant = get_object_or_404(Plant, pk=item_id)
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
                messages.success(request, f'Updated size {size.upper()} {plant.name} quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]["items_by_size"][size] = quantity
                messages.success(request, f'Added size{size.upper()} {plant.name} to your cart')
        else:
            cart[item_id] = {"items_by_size": {size: quantity}}
            messages.success(request, f'Added size{size.upper()} {plant.name} to your cart')
    else:

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {plant.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {plant.name} to your cart')

    request.session["cart"] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified plant to the specified amount"""
    
    plant = get_object_or_404(Plant, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    if "plant_size" in request.POST:
        size = request.POST["plant_size"]
    cart = request.session.get("cart", {})

    if size:
        if quantity > 0:
            cart[item_id]["items_by_size"][size] = quantity
            cart.pop[item_id]
            messages.success(request, f'Removed {plant.name} from your cart')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {plant.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {plant.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {plant.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        plant = get_object_or_404(plant, pk=item_id)
        size = None
        if 'plant_size' in request.POST:
            size = request.POST['plant_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {plant.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {plant.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500) 
