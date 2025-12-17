from django.shortcuts import render
from .serializers import UsuarioSerializer
from rest_framework import generics, permissions 
from rest_framework.response import Response 
from .models import Usuario
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import EsAdmin
# Create your views here.


@api_view(['GET'])
@permission_classes([EsAdmin])

def usuarios_admin(request):

    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many = True)

    return Response(serializer.data)
    
