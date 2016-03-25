from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    list_display = ('name', 'views', 'likes', 'slug')
    search_fields = ('name', 'slug')


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'category', 'views']
    list_display = ('title', 'category', 'views', 'url')
    list_filter = ('category', )
    search_fields = ['title', 'category']

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
