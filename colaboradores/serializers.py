from colaboradores.models import Colaborador
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class ColaboradorSerializer(GeoFeatureModelSerializer):
    horario = serializers.SerializerMethodField()
    identificador = serializers.SerializerMethodField()

    def get_horario(self, obj):
        return obj.get_horario_display()

    def get_identificador(self, obj):
        return "C-{}".format(obj.pk)

    class Meta:
        model = Colaborador
        geo_field = "geom"
        fields = '__all__'
