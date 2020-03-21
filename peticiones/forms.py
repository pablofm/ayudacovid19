from django.contrib.gis import forms
from peticiones.models import Peticion
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point


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
        return m

    class Meta:
        model = Peticion
        fields = '__all__'
        exclude = ['geom']
