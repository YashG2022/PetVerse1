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

def lion(request):
    return render(request,"pets/lion_selection.html")

def tiger(request):
    return render(request,"pets/tiger_selection.html")
