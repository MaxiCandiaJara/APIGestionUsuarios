from django.shortcuts import render
from API import forms
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

def main(request):
    
    form = forms.UsuarioForms(request.POST)



    return render(request, "main.html")