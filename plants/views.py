from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Plant


def all_plants(request):
    """A view to show all plants, including sorting and search queries """

    plants = Plant.objects.all()
    query = None

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
    }
    return render(request, 'plants/plants.html', context)


def plant_detail(request, plant_id):
    """A view to show plant details """

    plant = get_object_or_404(Plant, pk=plant_id)

    context = {
        'plant': plant,
    }
    return render(request, 'plants/plant_detail.html', context)






