from colaboradores.models import Colaborador, SolicitudAccesoColaborador
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class ColaboradorListSerializer(GeoFeatureModelSerializer):
    horario = serializers.SerializerMethodField()
    identificador = serializers.SerializerMethodField()

    def get_horario(self, obj):
        return obj.get_horario_display()

    def get_identificador(self, obj):
        return obj.pk

    class Meta:
        model = Colaborador
        geo_field = "geom"
        fields = ['nombre', 'horario', 'mensaje', 'horario', 'identificador']


class ColaboradorSerializer(GeoFeatureModelSerializer):
    horario = serializers.SerializerMethodField()
    identificador = serializers.SerializerMethodField()

    def get_horario(self, obj):
        return obj.get_horario_display()

    def get_identificador(self, obj):
        return obj.pk

    class Meta:
        model = Colaborador
        geo_field = "geom"
        fields = "__all__"


class SolicitudAccesoColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAccesoColaborador
        exclude = ("acceso_permitido", )
