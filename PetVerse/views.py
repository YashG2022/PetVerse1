from django.shortcuts import render


def home(request):
    # return(HttpResponse('<h1>Welcome to PetVerse</h1>'))
    return render(request,'webhome.html')

def about(request):
    # return(HttpResponse('<h1>Welcome to PetVerse</h1>'))
    return render(request,'about.html')

def help(request):
    # return(HttpResponse('<h1>Welcome to PetVerse</h1>'))
    return render(request,'help.html')
# Create your views here.


# myapp/views.py

