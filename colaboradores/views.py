from rest_framework import viewsets
from rest_framework import mixins
from colaboradores.models import Colaborador, SolicitudAccesoColaborador
from colaboradores.serializers import ColaboradorSerializer, ColaboradorListSerializer, SolicitudAccesoColaboradorSerializer


from django.views.generic.edit import CreateView
from colaboradores.forms import ContactarColaboradorForm, ColaboradorForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from base.emails import enviar_correo_acceso_datos


class APIColaboradoresView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Colaborador.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ColaboradorSerializer
        return ColaboradorListSerializer


class APIContactoColaboradorView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SolicitudAccesoColaborador.objects.all()
    serializer_class = SolicitudAccesoColaboradorSerializer


class CrearColaboradorView(CreateView):
    template_name = 'colaboradores/add.html'
    form_class = ColaboradorForm
    model = Colaborador
    success_url = reverse_lazy('datos_recibidos')


class SolicitarContactoColaboradorView(CreateView):
    template_name = 'colaboradores/contactar.html'
    form_class = ContactarColaboradorForm
    success_url = reverse_lazy('peticion_enviada')

    def get_context_data(self, **kwargs):
        context = super(SolicitarContactoColaboradorView, self).get_context_data(**kwargs)
        context['colaborador'] = get_object_or_404(Colaborador, pk=self.kwargs['pk'])
        return context


def permitirContacto(request):
    permitido = False
    nombre = None
    solicitud = None
    codigo = request.GET.get('codigo')

    if SolicitudAccesoColaborador.objects.filter(codigo_acceso=codigo).exists():
        solicitud = SolicitudAccesoColaborador.objects.get(codigo_acceso=codigo)

    if solicitud:
        solicitud.acceso_permitido = True
        solicitud.save()
        permitido = True
        nombre = solicitud.nombre

        # El colaborador da permiso para compartir sus datos. Se envían 2 correos:
        # El primero para el colaborador, con los datos de la persona que necesita ayuda
        datos_email_colaborador = {
            'nombre_para': solicitud.colaborador.nombre,
            'email_para': solicitud.colaborador.email,
            'nombre_contacto': solicitud.nombre,
            'telefono_contacto': solicitud.telefono,
            'email_contacto': solicitud.email,
            'mensaje_contacto': solicitud.mensaje,
        }
        enviar_correo_acceso_datos.delay(datos_email_colaborador)
        # El segundo para la persona necesitada, con los datos de la persona que le ofrece ayuda

        datos_email_solicitante = {
            'nombre_para': solicitud.nombre,
            'email_para': solicitud.email,
            'nombre_contacto': solicitud.colaborador.nombre,
            'telefono_contacto': solicitud.colaborador.telefono,
            'email_contacto': solicitud.colaborador.email,
            'mensaje_contacto': solicitud.colaborador.mensaje
        }
        enviar_correo_acceso_datos.delay(datos_email_solicitante)

    return render(request, 'base/validar_codigo.html', {"nombre": nombre, "permitido": permitido})
