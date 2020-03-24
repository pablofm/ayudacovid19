from peticiones.models import Peticion
from peticiones.serializers import PeticionSerializer
from rest_framework import viewsets
from django.views.generic.edit import CreateView
from peticiones.forms import PeticionForm, ContactarPeticionForm
from peticiones.models import SolicitudAccesoPeticion
from django.shortcuts import render
from django.urls import reverse_lazy


class APIColaboradoresView(viewsets.ReadOnlyModelViewSet):
    queryset = Peticion.objects.all()
    serializer_class = PeticionSerializer


class CrearPeticionView(CreateView):
    template_name = 'peticiones/add.html'
    form_class = PeticionForm
    model = Peticion
    success_url = reverse_lazy('datos_recibidos')


class SolicitarContactoPeticionView(CreateView):
    template_name = 'peticiones/contactar.html'
    form_class = ContactarPeticionForm
    success_url = reverse_lazy('peticion_enviada')

    def get_context_data(self, **kwargs):
        context = super(SolicitarContactoPeticionView, self).get_context_data(**kwargs)
        context['peticion'] = Peticion.objects.get(pk=self.kwargs['pk'])
        return context


def permitirContacto(request):
    permitido = False
    nombre = None
    solicitud = None
    codigo = request.GET.get('codigo')

    if SolicitudAccesoPeticion.objects.filter(codigo_acceso=codigo).exists():
        solicitud = SolicitudAccesoPeticion.objects.get(codigo_acceso=codigo)

    if solicitud:
        solicitud.acceso_permitido = True
        solicitud.save()
        permitido = True
        nombre = solicitud.nombre
        # TODO
        # En este punto la persona que necesita ayuda ha compartido sus datos.
        # Enviar mensaje al colaborador compartiendo los datos.
        # Por el momento será un proceso manual

    return render(request, 'base/validar_codigo.html', {"nombre": nombre, "permitido": permitido})
