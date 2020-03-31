from django.contrib.gis import forms
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
from colaboradores.models import Colaborador, SolicitudAccesoColaborador
from emails.emails import enviar_correo_pidiendo_ayuda
from emails.emails import enviar_correo_nuevo_colaborador
from emails.emails import enviar_correo_nueva_solicitud_colaborador


class ColaboradorForm(forms.ModelForm):
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        telefono = cleaned_data.get("telefono")
        email = cleaned_data.get("email")
        if not email and not telefono:
            raise ValidationError("Es necesario un método de contacto: email o teléfono")

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
        colaborador = super(ColaboradorForm, self).save(commit=False)
        colaborador.geom = Point(self.cleaned_data['lon'], self.cleaned_data['lat'], srid=4326)
        if commit:
            colaborador.save()
        enviar_correo_nuevo_colaborador.delay()
        return colaborador

    class Meta:
        model = Colaborador
        fields = '__all__'
        exclude = ['geom']


class ContactarColaboradorForm(forms.ModelForm):
    id_colaborador = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        telefono = cleaned_data.get("telefono")
        email = cleaned_data.get("email")
        if not email and not telefono:
            raise ValidationError("Es necesario un método de contacto: email o teléfono")

    def is_valid(self):
        valid = super(ContactarColaboradorForm, self).is_valid()
        if not valid:
            return valid
        if not self.data["email"] and not self.data["telefono"]:
            return False
        return True

    def save(self):
        contacto = super(ContactarColaboradorForm, self).save(commit=False)
        contacto.colaborador = Colaborador.objects.get(pk=self.cleaned_data['id_colaborador'])
        contacto.save()
        # Se envía un correo donde alquien que necesita ayuda solicita el acceso a los datos un colaborador.
        enviar_correo_nueva_solicitud_colaborador.delay()
        enviar_correo_pidiendo_ayuda.delay(contacto.pk)

        return contacto

    class Meta:
        model = SolicitudAccesoColaborador
        fields = '__all__'
        exclude = ['colaborador', 'codigo_acceso', 'acceso_permitido']
