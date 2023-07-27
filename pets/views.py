from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm
from .models import MyFormData
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

def queryform(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data here
            name = form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the data (e.g., save to database)
            MyFormData.objects.create(name=name, phone=phone, email=email, message=message)

            # Redirect to a success page or render a success template
            return render(request, 'pets/successform.html', {'name': name})
    else:
        form = MyForm()

    return render(request, 'pets/queryform.html', {'form': form})