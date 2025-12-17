from django.shortcuts import render
from API import forms

def base(request):
    
    return render(request, "base.html")