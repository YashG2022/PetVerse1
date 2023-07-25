from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return(HttpResponse('<h1>Welcome to Pet food shop</h1>'))

# Create your views here.
