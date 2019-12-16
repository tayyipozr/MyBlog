from django.contrib import admin
from .models import Pictures

class PictureAdmin(admin.ModelAdmin):
    list_display = ('id','picture_name','date')
    list_display_links = ('id', 'picture_name')
    list_filter = ('date',)
    search_fields = ('picture_name', 'picture_description')
    list_per_page = 20

# Register your models here.

admin.site.register(Pictures, PictureAdmin)

