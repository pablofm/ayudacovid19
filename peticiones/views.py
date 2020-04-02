from peticiones.models import Peticion, SolicitudAccesoPeticion
from django.views.generic.edit import CreateView
from peticiones.forms import PeticionForm, ContactarPeticionForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from emails.emails import enviar_correo_acceso_datos
from django.http import HttpResponseRedirect


class CrearPeticionView(CreateView):
    template_name = 'peticiones/add.html'
    form_class = PeticionForm
    model = Peticion
    success_url = reverse_lazy('datos_recibidos')


class SolicitarContactoPeticionView(CreateView):
    template_name = 'peticiones/contactar.html'
    form_class = ContactarPeticionForm
    success_url = reverse_lazy('acceso_solicitado')

    def get(self, request, *args, **kwargs):
        peticion = get_object_or_404(Peticion, pk=self.kwargs['pk'])
        if peticion.atendida:
            return HttpResponseRedirect(reverse_lazy('peticion_atendida'))
        else:
            context = {
                'peticion': peticion,
                'form': self.form_class
            }
            return render(request, self.template_name, context)


def permitirContacto(request):
    codigo = request.GET.get('codigo')
    solicitud = get_object_or_404(SolicitudAccesoPeticion, codigo_acceso=codigo)
    # La persona necesitada da permiso para compartir sus datos. Se envían 2 correos:
    # El primero para el colaborador, con los datos de la persona que necesita ayuda
    datos_email_colaborador = {
        'nombre_para': solicitud.nombre,
        'email_para': solicitud.email,
        'nombre_contacto': solicitud.peticion.nombre,
        'telefono_contacto': str(solicitud.peticion.telefono),
        'email_contacto': solicitud.peticion.email,
        'mensaje_contacto': solicitud.peticion.mensaje
    }
    enviar_correo_acceso_datos.delay(datos_email_colaborador)

    # El segundo para la persona necesitada, con los datos de la persona que le ofrece ayuda
    datos_email_solicitante = {
        'nombre_para': solicitud.peticion.nombre,
        'email_para': solicitud.peticion.email,
        'nombre_contacto': solicitud.nombre,
        'telefono_contacto': str(solicitud.telefono),
        'email_contacto': solicitud.email,
        'mensaje_contacto': solicitud.mensaje
    }
    enviar_correo_acceso_datos.delay(datos_email_solicitante)
    solicitud.acceso_permitido = True
    solicitud.save()

    return render(request, 'base/validar_codigo.html', {"nombre": solicitud.nombre})
