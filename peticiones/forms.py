from django.contrib.gis import forms
from peticiones.models import Peticion, SolicitudAccesoPeticion
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
from base.emails import enviar_correo_ofreciendo_ayuda, enviar_correo_nueva_peticion, enviar_correo_nueva_solicitud_peticion


class PeticionForm(forms.ModelForm):
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)

    def clean_lat(self):
        lat = self.cleaned_data['lat']
        if not lat:
            raise ValidationError("Indica donde estás")
        return lat

    def is_valid(self):
        valid = super(PeticionForm, self).is_valid()
        if not valid:
            return valid
        if not self.data["email"] and not self.data["telefono"]:
            return False
        return True

    def save(self, commit=True):
        m = super(PeticionForm, self).save(commit=False)
        m.geom = Point(self.cleaned_data['lon'], self.cleaned_data['lat'], srid=4326)
        if commit:
            m.save()
        enviar_correo_nueva_peticion()
        return m

    class Meta:
        model = Peticion
        fields = '__all__'
        exclude = ['geom']


class ContactarPeticionForm(forms.ModelForm):
    id_peticion = forms.IntegerField(required=False)

    def save(self):
        contacto = super(ContactarPeticionForm, self).save(commit=False)
        contacto.peticion = Peticion.objects.get(pk=self.cleaned_data['id_peticion'])
        contacto.save()
        # Se envía un correo donde alquien quiere ayuda a una persona necesitada y solicita el acceso a sus datos.
        datos_email = {
            'peticion':  contacto.peticion.nombre,
            'email': contacto.peticion.email,
            'nombre':  contacto.nombre,
            'mensaje':  contacto.mensaje,
            'enlace': contacto.url_autorizacion()
        }
        enviar_correo_ofreciendo_ayuda(datos_email)
        enviar_correo_nueva_solicitud_peticion()
        return contacto

    class Meta:
        model = SolicitudAccesoPeticion
        fields = '__all__'
        exclude = ['peticion', 'codigo_acceso', 'acceso_permitido']
