from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^search/$', views.search, name='search'),
        url(r'^goto/$', views.track_url, name='goto'),
        url(r'^add_profile/$', views.register_profile, name='add_profile'),
        url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
        url(r'^profile/(?P<user_name>[\w]+)/$', views.user_area, name='user_area'),
        url(r'^like_category/$', views.like_category, name='like_category'),
        ]
