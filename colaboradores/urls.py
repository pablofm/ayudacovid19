from colaboradores import views as colaboradores_views
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register('API/colaboradores', colaboradores_views.APIColaboradoresView)
router.register('API/colaboradores/acceso', colaboradores_views.APIContactoColaboradorView)

urlpatterns = [
    path('colaboradores/add/', colaboradores_views.CrearColaboradorView.as_view(), name='crear-colaborador'),
    path('colaboradores/<pk>/contactar/', colaboradores_views.SolicitarContactoColaboradorView.as_view(), name='contactar-colaborador'),
    path('colaboradores/validar/', colaboradores_views.permitirContacto, name='validar-acceso-colaborador'),
]

urlpatterns += router.urls
