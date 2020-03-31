from colaboradores.models import Colaborador, SolicitudAccesoColaborador
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class ColaboradorListSerializer(GeoFeatureModelSerializer):
    horario_verbose = serializers.SerializerMethodField()

    def get_horario_verbose(self, obj):
        return obj.get_horario_display()

    def get_identificador(self, obj):
        return obj.pk

    def validate(self, data):
        if "email" not in data and "telefono" not in data:
            raise serializers.ValidationError("Es necesario un método de contacto: email o teléfono")
        return data

    class Meta:
        model = Colaborador
        geo_field = "geom"
        fields = ['nombre', 'horario', 'mensaje', 'horario', 'id', 'horario_verbose']


class ColaboradorSerializer(ColaboradorListSerializer):

    class Meta:
        model = Colaborador
        geo_field = "geom"
        exclude = ("creacion", )


class SolicitudAccesoColaboradorSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if "email" not in data and "telefono" not in data:
            raise serializers.ValidationError("Es necesario un método de contacto: email o teléfono")
        return data

    class Meta:
        model = SolicitudAccesoColaborador
        exclude = ("acceso_permitido", "codigo_acceso", "creacion")
