from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('repeater', views.repeaters, name='repeaters'),
    path('repeater/new', views.repeater_new, name='repeater_new'),
]
