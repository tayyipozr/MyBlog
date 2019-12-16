from django.db import models

# Create your models here.

class Pictures(models.Model):
    picture_name = models.CharField(max_length=20)
    place_of_picture = models.CharField(max_length=30)
    picture_description = models.CharField(max_length=200)
    picture_url = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

