from django.shortcuts import render
from django.utils.http import content_disposition_header
from .models import Plant

def all_plants(request):
    """A view to show all products, including sorting and search queries """

    plants = Plant.objects.all()

    context = {
        'plants': plants,
    }
    return render(request, 'plants/plants.html', context)
