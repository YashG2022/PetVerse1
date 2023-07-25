from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return(HttpResponse('<h1>Welcome to Pet adoption shop</h1>'))
    return render(request,"pets/animal_selection.html")
# Create your views here.

def dog(request):
    return render(request,"pets/dog_selection.html")

def cat(request):
    return render(request,"pets/cat_selection.html")

def rabbit(request):
    return render(request,"pets/rabbit_selection.html")

def bird(request):
    return render(request,"pets/bird_selection.html")

def fish(request):
    return render(request,"pets/fish_selection.html")
