from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date','isPublished', 'slug')
    list_display_links = ('id', 'name', 'slug')
    list_filter = ('created_date',)
    list_editable = ('isPublished',)
    search_fields = ('name', 'description')
    list_per_page = 20


# Register your models here.

admin.site.register(Article, ArticleAdmin)