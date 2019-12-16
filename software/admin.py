from django.contrib import admin
from .models import Softwares

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('id','title','date')
    list_display_links = ('id', 'title')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    list_per_page = 20


# Register your models here.

admin.site.register(Softwares, SoftwareAdmin)