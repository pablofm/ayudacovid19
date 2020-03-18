from colaboradores.models import Colaborador
from colaboradores.serializers import ColaboradorSerializer
from rest_framework import viewsets


class ColaboradoresAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
