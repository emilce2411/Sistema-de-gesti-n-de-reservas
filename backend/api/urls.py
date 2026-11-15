from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ReservaViewSet

# Creamos el enrutador automático para nuestros ViewSets
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]