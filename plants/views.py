from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Plant, Category


def all_plants(request):
    """A view to show all plants, including sorting and search queries """

    plants = Plant.objects.all()
    query = ""
    categories = ""


    if request.GET:
        print('request.get', request.GET)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            plants = plants.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('plants'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        plants = plants.filter(queries)

    context = {
        'plants': plants,
        'search_term': query,
        'current_categories': categories,
    }
    return render(request, 'plants/plants.html', context)


def plant_detail(request, plant_id):
    """A view to show plant details """

    plant = get_object_or_404(Plant, pk=plant_id)

    context = {
        'plant': plant,
    }
    return render(request, 'plants/plant_detail.html', context)






