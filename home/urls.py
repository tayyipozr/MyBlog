from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'home'),
    path('<str:article_slug>', views.details, name= 'detail'),
    path('search', views.search, name= 'search'),
]