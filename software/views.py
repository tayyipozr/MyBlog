from django.shortcuts import render
from .models import Softwares

# Create your views here.

def software(request):
    softwares = Softwares.objects.all()
    context = {
        'softwares' : softwares
    }
    return render(request, 'software/software.html', context)