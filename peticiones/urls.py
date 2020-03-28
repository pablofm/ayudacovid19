from peticiones import views as peticiones_views
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()
router.register('API/peticiones', peticiones_views.APIColaboradoresView)
router.register('API/peticiones/acceso', peticiones_views.APIContactoPeticionView)


urlpatterns = [
    path('peticiones/add/', peticiones_views.CrearPeticionView.as_view(), name='crear-peticion'),
    path('peticiones/<pk>/contactar/', peticiones_views.SolicitarContactoPeticionView.as_view(), name='contactar-peticion'),
    path('peticiones/validar/', peticiones_views.permitirContacto, name='validar-acceso-peticion'),
]

urlpatterns += router.urls
