from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'home'),
    path('<int:home_id>', views.details, name= 'detail'),
    path('search', views.search, name= 'search'),
]