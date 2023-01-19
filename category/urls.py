from django.urls import path, re_path
from . import views


app_name = 'category'
urlpatterns = [
    path('', views.list_parent, name='list_parent'),
    re_path(r'(?P<slug>[-\w]+)/', views.list_child, name='list_child'),
]
