from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all/$', views.post_list, name='post_list'),
    url(r'^$', views.post_new, name='post_new'),
    url(r'^create/$', views.post_create, name='post_create'),
]
