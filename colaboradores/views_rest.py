from rest_framework import viewsets
from rest_framework import mixins
from colaboradores.models import Colaborador
from colaboradores.models import SolicitudAccesoColaborador
from colaboradores.serializers import ColaboradorSerializer
from colaboradores.serializers import ColaboradorListSerializer
from colaboradores.serializers import SolicitudAccesoColaboradorSerializer
from fuentes.api import actualizar_fuente
from emails.emails import enviar_correo_nuevo_colaborador
from emails.emails import enviar_correo_nueva_solicitud_colaborador
from emails.emails import enviar_correo_pidiendo_ayuda


class APIColaboradoresView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Colaborador.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ColaboradorSerializer
        return ColaboradorListSerializer

    def perform_create(self, serializer):
        if "key" in self.request.data:
            actualizar_fuente(self.request.data["key"])
        serializer.save()
        enviar_correo_nuevo_colaborador.delay()


class APIContactoColaboradorView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SolicitudAccesoColaborador.objects.all()
    serializer_class = SolicitudAccesoColaboradorSerializer

    def perform_create(self, serializer):
        if "key" in self.request.data:
            actualizar_fuente(self.request.data["key"])
        contacto = serializer.save()
        enviar_correo_nueva_solicitud_colaborador.delay()
        enviar_correo_pidiendo_ayuda.delay(contacto.pk)
