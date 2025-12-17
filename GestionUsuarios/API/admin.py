from django.contrib import admin
from .models import Usuario
# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

    list_display = ['id', 'nombre', 'apellidos', 'rol']

    search_fields = ['nombre',]

    list_filter = ['rol',]
