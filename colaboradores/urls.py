from colaboradores import views as colaboradores_views
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register('', colaboradores_views.APIColaboradoresView)

urlpatterns = [
    path('add/', colaboradores_views.CrearColaboradorView.as_view(), name='colaborador-add'),
    path('<pk>/contactar/', colaboradores_views.SolicitarContactoColaboradorView.as_view(), name='contactar-colaborador'),
    path('validar/', colaboradores_views.permitirContacto, name='validar-acceso-colaborador'),
]

urlpatterns += router.urls
