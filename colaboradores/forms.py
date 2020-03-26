from django.contrib.gis import forms
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
from django.core.validators import RegexValidator
from colaboradores.models import Colaborador, SolicitudAccesoColaborador
from base.emails import enviar_correo_pidiendo_ayuda

validar_telefono = RegexValidator(r'^(\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')


class ColaboradorForm(forms.ModelForm):
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)

    def clean_lat(self):
        lat = self.cleaned_data['lat']
        if not lat:
            raise ValidationError("Indica donde estás")
        return lat

    def is_valid(self):
        valid = super(ColaboradorForm, self).is_valid()
        if not valid:
            return valid
        if not self.data["email"] and not self.data["telefono"]:
            return False
        return True

    def save(self, commit=True):
        m = super(ColaboradorForm, self).save(commit=False)
        m.geom = Point(self.cleaned_data['lon'], self.cleaned_data['lat'], srid=4326)
        if commit:
            m.save()
        return m

    class Meta:
        model = Colaborador
        fields = '__all__'
        exclude = ['geom']


class ContactarColaboradorForm(forms.ModelForm):

    id_colaborador = forms.IntegerField(required=False)

    def save(self):
        contacto = super(ContactarColaboradorForm, self).save(commit=False)
        contacto.colaborador = Colaborador.objects.get(pk=self.cleaned_data['id_colaborador'])
        contacto.save()
        # Se envía un correo donde alquien que necesita ayuda solicita el acceso a los datos un colaborador.
        datos_email = {
            'colaborador':  contacto.colaborador.nombre,
            'email': contacto.colaborador.email,
            'nombre':  contacto.nombre,
            'mensaje':  contacto.mensaje,
            'enlace': contacto.url_autorizacion()
        }
        enviar_correo_pidiendo_ayuda(datos_email)
        return contacto

    class Meta:
        model = SolicitudAccesoColaborador
        fields = '__all__'
        exclude = ['colaborador', 'codigo_acceso', 'acceso_permitido']
