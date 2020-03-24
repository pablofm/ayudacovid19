from peticiones import views as peticiones_views
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()
router.register('', peticiones_views.APIColaboradoresView)

urlpatterns = [
    path('add/', peticiones_views.CrearPeticionView.as_view(), name='peticion-add'),
    path('<pk>/contactar/', peticiones_views.SolicitarContactoPeticionView.as_view(), name='contactar-peticion'),
    path('validar/', peticiones_views.permitirContacto, name='validar-acceso-peticion'),
]

urlpatterns += router.urls
