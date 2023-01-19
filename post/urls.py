from django.urls import path, re_path
from . import views


app_name = 'post'
urlpatterns = [
    path('', views.list, name='list_post'),
    re_path(r'(?P<pk>[-\w]+)/(?P<slug>[-\w]+)/',
            views.detail, name='detail_post'),
]
