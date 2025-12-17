from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):

    ROLES = (
        
        ('admin', 'Administrador'),
        ('user', 'Usuario'),

    )

    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    rol = models.CharField(max_length=20, choices=ROLES, default='user')

    def __str__(self):

        info = f'{self.nombre} {self.apellidos} ({self.rol})'

        return info
    


