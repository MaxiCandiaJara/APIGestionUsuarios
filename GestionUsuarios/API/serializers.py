from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = [
            'id',
            'username',
            'nombre',
            'apellidos',
            'rol',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            nombre=validated_data['nombre'],
            apellidos=validated_data['apellidos'],
            rol=validated_data.get('rol', 'user')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
