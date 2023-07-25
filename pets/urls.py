from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='example-view'),
    path('dog',views.dog,name='dog-list-page'),
    path('cat',views.cat,name='cat-list-page'),
    path('rabbit',views.rabbit,name='rabbit-list-page'),
    path('bird',views.bird,name='lion-list-page'),
    path('fish',views.fish,name='tiger-list-page'),
]
