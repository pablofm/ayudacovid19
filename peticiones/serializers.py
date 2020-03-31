from peticiones.models import Peticion, SolicitudAccesoPeticion
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class PeticionListSerializer(GeoFeatureModelSerializer):
    def validate(self, data):
        if "email" not in data and "telefono" not in data:
            raise serializers.ValidationError("Es necesario un método de contacto: email o teléfono")
        return data

    class Meta:
        model = Peticion
        geo_field = "geom"
        fields = ['nombre', 'mensaje', 'id']


class PeticionSerializer(PeticionListSerializer):
    class Meta:
        model = Peticion
        geo_field = "geom"
        exclude = ("creacion", )


class SolicitudAccesoPeticionSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if "email" not in data and "telefono" not in data:
            raise serializers.ValidationError("Es necesario un método de contacto: email o teléfono")
        return data

    class Meta:
        model = SolicitudAccesoPeticion
        exclude = ("acceso_permitido", "codigo_acceso", "creacion")
