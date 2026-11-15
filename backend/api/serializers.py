from rest_framework import serializers
from .models import Usuario, Reserva

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'password', 'rol']
        extra_kwargs = {'password': {'write_only': True}}

class ReservaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='usuario.nombre')

    class Meta:
        model = Reserva
        fields = ['id', 'fecha', 'hora_inicio', 'hora_fin', 'estado', 'usuario', 'usuario_nombre']