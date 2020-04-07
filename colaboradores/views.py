from colaboradores.models import Colaborador, SolicitudAccesoColaborador
from django.views.generic.edit import CreateView
from colaboradores.forms import ContactarColaboradorForm, ColaboradorForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from emails.emails import enviar_correo_acceso_datos
from django.http import JsonResponse


class CrearColaboradorView(CreateView):
    template_name = 'colaboradores/add.html'
    form_class = ColaboradorForm
    model = Colaborador
    success_url = reverse_lazy('datos_recibidos')


class SolicitarContactoColaboradorView(CreateView):
    template_name = 'colaboradores/contactar.html'
    form_class = ContactarColaboradorForm
    success_url = reverse_lazy('acceso_solicitado')

    def get_context_data(self, **kwargs):
        context = super(SolicitarContactoColaboradorView, self).get_context_data(**kwargs)
        context['colaborador'] = get_object_or_404(Colaborador, pk=self.kwargs['pk'])
        return context


def permitirContacto(request):
    codigo = request.GET.get('codigo')
    solicitud = get_object_or_404(SolicitudAccesoColaborador, codigo_acceso=codigo)
    # El colaborador da permiso para compartir sus datos. Se envían 2 correos:
    # El primero para el colaborador, con los datos de la persona que necesita ayuda
    datos_email_colaborador = {
        'nombre_para': solicitud.colaborador.nombre,
        'email_para': solicitud.colaborador.email,
        'nombre_contacto': solicitud.nombre,
        'telefono_contacto': str(solicitud.telefono),
        'email_contacto': solicitud.email,
        'mensaje_contacto': solicitud.mensaje,
    }
    enviar_correo_acceso_datos.delay(datos_email_colaborador)
    # El segundo para la persona necesitada, con los datos de la persona que le ofrece ayuda

    datos_email_solicitante = {
        'nombre_para': solicitud.nombre,
        'email_para': solicitud.email,
        'nombre_contacto': solicitud.colaborador.nombre,
        'telefono_contacto': str(solicitud.colaborador.telefono),
        'email_contacto': solicitud.colaborador.email,
        'mensaje_contacto': solicitud.colaborador.mensaje
    }
    enviar_correo_acceso_datos.delay(datos_email_solicitante)
    solicitud.acceso_permitido = True
    solicitud.save()

    return render(request, 'base/validar_codigo.html', {"nombre": solicitud.nombre})


def solicitudes(request):
    return JsonResponse({'solicitudes': SolicitudAccesoColaborador.objects.count()})
