from colaboradores.models import Colaborador
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class ColaboradorSerializer(GeoFeatureModelSerializer):
    horario = serializers.SerializerMethodField()

    def get_horario(self, obj):
        return obj.get_horario_display()

    class Meta:
        model = Colaborador
        geo_field = "geom"
        fields = '__all__'
