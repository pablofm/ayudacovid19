from rest_framework import viewsets
from colaboradores.models import Colaborador, SolicitudAccesoColaborador
from colaboradores.serializers import ColaboradorSerializer
from django.views.generic.edit import CreateView
from colaboradores.forms import ContactarColaboradorForm, ColaboradorForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class APIColaboradoresView(viewsets.ReadOnlyModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer


class CrearColaboradorView(CreateView):
    template_name = 'colaboradores/add.html'
    form_class = ColaboradorForm
    model = Colaborador
    success_url = reverse_lazy('datos_recibidos')


class SolicitarContactoColaboradorView(CreateView):
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Hello, World!')

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
        # TODO
        # En este punto el colaborador ha compartido sus datos.
        # Enviar mensaje a la persona que necesita ayuda compartiendo los datos.
        # Por el momento será un proceso manual

    return render(request, 'base/validar_codigo.html', {"nombre": nombre, "permitido": permitido})
