from django.test import TestCase
from colaboradores.forms import ColaboradorForm
from faker import Faker
fake = Faker('es_ES')


class ColaboradorFormTest(TestCase):
    def setUp(self):
        self.datos_formulario = {
            'lat': fake.latitude(),
            'lon': fake.longitude(),
            'nombre': fake.name(),
            'email': fake.email(),
            'telefono': '666666666',
            'horario': '0',
            'servicios': fake.paragraphs(nb=3)
        }

    def test_formulario_vacio_no_es_valido(self):
        form = ColaboradorForm()
        self.assertFalse(form.is_valid())

    def test_formulario_sin_email_es_valido(self):
        self.datos_formulario['email'] = None
        form = ColaboradorForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_sin_telefono_es_valido(self):
        self.datos_formulario['telefono'] = None
        form = ColaboradorForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_requiere_o_telefono_o_email(self):
        self.datos_formulario['telefono'] = None
        self.datos_formulario['email'] = None
        form = ColaboradorForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())
