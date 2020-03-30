from rest_framework import viewsets
from rest_framework import mixins
from comercios.models import Comercio
from comercios.serializers import ComercioSerializer
from fuentes.api import actualizar_fuente
from emails.emails import enviar_correo_nuevo_comercio


class APIComerciosView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Comercio.objects.all()
    serializer_class = ComercioSerializer

    def perform_create(self, serializer):
        if "key" in self.request.data:
            actualizar_fuente(self.request.data["key"])
        serializer.save()
        enviar_correo_nuevo_comercio.delay()
