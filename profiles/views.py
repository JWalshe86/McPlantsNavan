from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """Display the user's profile and handle profile updates."""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True,
    }
    template = "profiles/profile.html"

    return render(request, template, context)


def order_history(request, order_number):
    """Display the order history for a specific order number."""

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    context = {
        "order": order,
        "from_profile": True,
    }
    template = "checkout/checkout_success.html"

    return render(request, template, context)

