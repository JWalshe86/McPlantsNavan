from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Category, Plant, PlantReview, SeasonalEvent, Stock
from .forms import PlantForm, ReviewForm, EventForm


def all_plants(request):
    """A view to show all plants, including sorting and search queries"""

    plants = Plant.objects.all()
    query = ""
    categories = ""
    sort = ""
    direction = ""

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                plants = plants.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
                plants = plants.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            plants = plants.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("plants"))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        plants = plants.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "plants": plants,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }
    return render(request, "plants/plants.html", context)


def plant_detail(request, plant_id):
    """A view to show plant details"""

    plant = get_object_or_404(Plant, pk=plant_id)

    context = {
        "plant": plant,
    }
    return render(request, "plants/plant_detail.html", context)


@login_required
def add_plant(request):
    """Add a plant to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            messages.success(request, "Successfully added plant!")
            return redirect(reverse("plant_detail", args=[plant.id]))
        else:
            messages.error(
                request,
                "Failed to add plant. Please ensure the form is valid.",
            )
    else:
        form = PlantForm()

    template = "plants/add_plant.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_plant(request, plant_id):
    """Edit a plant in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated plant!")
            return redirect(reverse("plant_detail", args=[plant.id]))
        else:
            messages.error(
                request,
                "Failed to update plant. Please ensure the form is valid.",
            )
    else:
        form = PlantForm(instance=plant)
        messages.info(request, f"You are editing {plant.name}")

    template = "plants/edit_plant.html"
    context = {
        "form": form,
        "plant": plant,
    }

    return render(request, template, context)


@login_required
def delete_plant(request, plant_id):
    """Delete a plant from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    plant = get_object_or_404(Plant, pk=plant_id)
    plant.delete()
    messages.success(request, "Plant deleted!")
    return redirect(reverse("plants"))


# Review views


def all_reviews(request):
    """A view to show all reviews"""
    reviews = PlantReview.objects.all()

    context = {
        "reviews": reviews,
    }
    return render(request, "plants/reviews.html", context)


def review_detail(request, review_id):
    """A view to show review details"""

    review = get_object_or_404(PlantReview, pk=review_id)

    context = {
        "review": review,
    }
    return render(request, "plants/review_detail.html", context)


class add_review(CreateView):
    """A view to add reviews"""

    model = PlantReview
    fields = ["plant", "review", "rating"]
    success_url = reverse_lazy("reviews")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(add_review, self).form_valid(form)


@login_required
def edit_review(request, review_id):
    "A view to edit a review"
    review = get_object_or_404(PlantReview, pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated review!")
            return redirect(reverse("plant_detail", args=[review.id]))
        else:
            messages.error(
                request,
                "Failed to update review. Please ensure the form is valid.",
            )
    else:
        form = ReviewForm(instance=review)
        messages.info(request, "Your are editing your review")

        template = "plants/edit_review.html"
        context = {
            "form": form,
            "review": review,
        }
        return render(request, template, context)


def delete_review(request, review_id):
    """Delete a review from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    review = get_object_or_404(PlantReview, pk=review_id)
    review.delete()
    messages.success(request, "Review deleted!")
    return redirect(reverse("reviews"))


# Seasonal Events


def all_events(
    request,
):
    """A view to List Season Events"""
    events = SeasonalEvent.objects.all()

    context = {
        "events": events,
    }
    return render(request, "plants/events.html", context)


@staff_member_required
def add_event(request):
    """A view to add events"""

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, "Successfully added event!")
            return redirect(reverse("event_detail", args=[event.id]))
        else:
            messages.error(
                request,
                "Failed to add event. Please ensure the form is valid.",
            )

    else:
        form = EventForm()

    template = "plants/add_event.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def event_detail(request, event_id):
    """A view to show event details"""

    event = get_object_or_404(SeasonalEvent, pk=event_id)

    context = {
        "event": event,
    }
    return render(request, "plants/event_detail.html", context)


@login_required
def edit_event(request, event_id):
    """Edit a plant in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    event = get_object_or_404(SeasonalEvent, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated event!")
            return redirect(reverse("event_detail", args=[event.id]))
        else:
            messages.error(
                request,
                "Failed to update event. Please ensure the form is valid.",
            )
    else:
        form = EventForm(instance=event)
        messages.info(request, f"You are editing {event.name}")

    template = "plants/edit_event.html"
    context = {
        "form": form,
        "event": event,
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """Delete an event from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    event = get_object_or_404(SeasonalEvent, pk=event_id)
    event.delete()
    messages.success(request, "Event deleted!")
    return redirect(reverse("all_events"))


@staff_member_required
def stock_display(
    request,
):
    """List Stock"""
    stocks = Stock.objects.all()

    context = {
        "stocks": stocks,
    }
    return render(request, "plants/stock.html", context)
