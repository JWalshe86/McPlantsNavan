from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Category, Plant, PlantReview
from .forms import PlantForm, ReviewForm


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


def add_review(request, plant_id):

    review = get_object_or_404(PlantReview, pk=plant_id)
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added review!")
            return redirect("plant_detail", args=[plant.id])
        else:
            messages.error(
                request,
                "Failed to add review. Please ensure the form is valid.",
            )

    else:
        form = ReviewForm()

    template = "plants/add_review.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
