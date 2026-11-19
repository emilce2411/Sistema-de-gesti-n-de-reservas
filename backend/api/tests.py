from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Usuario, Reserva

class UsuarioAPITestCase(APITestCase):
    def setUp(self):
        self.usuario_data = {
            'nombre': 'Juan Pérez',
            'email': 'juan@example.com',
            'password': 'password123',
            'rol': 'cliente'
        }
        self.usuario = Usuario.objects.create(**self.usuario_data)
        self.list_url = reverse('usuario-list')

    def test_get_usuarios(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_usuario(self):
        data = {
            'nombre': 'Ana Gómez',
            'email': 'ana@example.com',
            'password': 'securepassword',
            'rol': 'cliente'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 2)


class ReservaAPITestCase(APITestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Carlos Test',
            email='carlos@example.com',
            password='123',
            rol='cliente'
        )
        self.reserva_data = {
            'fecha': '2026-12-01',
            'hora_inicio': '10:00:00',
            'hora_fin': '12:00:00',
            'estado': 'Confirmada',
            'usuario': self.usuario  
        }
        self.list_url = reverse('reserva-list')

    def test_get_reservas(self):
        Reserva.objects.create(**self.reserva_data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_reserva(self):
        
        data_api = {
            'fecha': '2026-12-01',
            'hora_inicio': '10:00:00',
            'hora_fin': '12:00:00',
            'estado': 'Confirmada',
            'usuario': self.usuario.id
        }
        response = self.client.post(self.list_url, data_api, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reserva.objects.count(), 1)