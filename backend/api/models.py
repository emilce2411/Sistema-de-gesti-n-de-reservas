from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=50, default='cliente')

    def __str__(self):
        return f"{self.nombre} ({self.email})"


class Reserva(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=50, default='Confirmada')
    # Relación de Uno a Muchos (ForeignKey): Un usuario puede tener muchas reservas
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva de {self.usuario.nombre} el {self.fecha} ({self.hora_inicio} - {self.hora_fin})"