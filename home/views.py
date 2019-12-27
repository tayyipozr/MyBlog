from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    articles = reversed(articles)
    
    context = {
        'articles' : articles
    }
    return render(request, 'home/list.html', context)

def details(request, article_slug):
    #try:
    #    article = Article.objects.get(pk = article_slug)
    #except Article.DoesNotExist:
    #    raise Http404('Yazı bulunamadı...')

    article = get_object_or_404(Article, slug= article_slug)
    context = {
        'article': article
    }
    return render(request, 'home/detail.html', context)

def search(request):
    return render(request, 'home/search.html')

