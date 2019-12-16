from django.shortcuts import render
from .models import Pictures

# Create your views here.

def postcard(request):
    pictures = Pictures.objects.all()

    context = {
        'pictures' : pictures
    }
    return render(request, 'postcard/postcard.html', context)