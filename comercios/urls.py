from comercios import views as comercios_views
from comercios import views_rest as comercios_rest
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()
urlpatterns = [
    path('comercios/add', comercios_views.CrearComercioView.as_view(), name='crear-comercio'),
]

router.register('API/comercios', comercios_rest.APIComerciosView)

urlpatterns += router.urls
