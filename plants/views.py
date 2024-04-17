from django.shortcuts import get_object_or_404, render
from .models import Plant

def all_plants(request):
    """A view to show all plants, including sorting and search queries """

    plants = Plant.objects.all()

    context = {
        'plants': plants,
    }
    return render(request, 'plants/plants.html', context)

def plant_detail(request, plant_id):
    """A view to show plant details """

    plant = get_object_or_404(Plant, pk=plant_id)

    context = {
        'plant': plant,
    }
    return render(request, 'plants/plant_detail.html', context)






