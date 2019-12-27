from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of Article')
    slug = models.CharField(max_length=50, verbose_name='Slug')
    description = models.TextField(verbose_name='Content of Article')
    image = models.CharField(max_length=50, verbose_name='Path of Image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of Creating')
    isPublished = models.BooleanField(default= True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return self.image