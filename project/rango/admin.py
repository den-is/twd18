from django.contrib import admin
from .models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    list_display = ('name', 'views', 'likes', 'slug')
    search_fields = ('name', 'slug')


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'category', 'views']
    list_display = ('title', 'category', 'views', 'url')
    list_filter = ('category', )
    search_fields = ['title', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
