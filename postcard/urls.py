from django.urls import path
from . import views

urlpatterns = [
        path('', views.postcard, name= 'postcard'),
]