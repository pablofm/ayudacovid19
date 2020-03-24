import factory
from colaboradores.models import Colaborador
from django.contrib.gis.geos import Point
from faker import Faker
fake = Faker('es_ES')


class ColaboradorFactory(factory.Factory):
    class Meta:
        model = Colaborador

    geom = Point(float(fake.longitude()), float(fake.latitude()), srid=4326)
    nombre = fake.name()
    telefono = '666666666'
    email = fake.email(),
    horario = '1'
    servicios = fake.paragraphs(nb=3)
