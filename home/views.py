from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    articles = reversed(articles)
    
    context = {
        'articles' : articles
    }
    return render(request, 'home/list.html', context)

def details(request):
    return render(request, 'home/detail.html')

def search(request):
    return render(request, 'home/search.html')

