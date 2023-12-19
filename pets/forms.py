# myapp/forms.py

from django import forms

class MyForm(forms.Form):
    # Define form fields here
    name = forms.CharField(max_length=100)
    phone=forms.CharField(max_length=12)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    # Add more fields as needed
