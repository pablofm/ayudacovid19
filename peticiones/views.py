from peticiones.models import Peticion
from peticiones.serializers import PeticionSerializer
from rest_framework import viewsets


class PeticionesAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Peticion.objects.all()
    serializer_class = PeticionSerializer
