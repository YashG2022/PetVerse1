from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='example-view'),
    path('dog',views.dog,name='dog-list-page'),
    path('cat',views.cat,name='cat-list-page'),
    path('rabbit',views.rabbit,name='bird-list-page'),
    path('lion',views.lion,name='lion-list-page'),
    path('tiger',views.tiger,name='tiger-list-page'),
]
