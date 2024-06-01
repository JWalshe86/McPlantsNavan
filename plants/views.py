from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Category, Plant
from .forms import PlantForm


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


def add_plant(request):
    """Add a plant to the store"""
    form = PlantForm()
    template = "plants/add_plant.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
