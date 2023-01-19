from django.urls import path, re_path
from . import views


app_name = 'course'
urlpatterns = [
    path('', views.list, name='list_course'),
    re_path(r'(?P<pk>[-\w]+)/(?P<slug>[-\w]+)/',
            views.detail, name='detail_course'),
]
