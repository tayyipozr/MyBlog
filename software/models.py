from django.db import models

# Create your models here.

class Softwares(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    link_name = models.CharField(max_length=20)
    size = models.CharField(max_length=8)