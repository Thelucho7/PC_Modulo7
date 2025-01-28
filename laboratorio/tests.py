from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio

# Create your tests here.


class LaboratorioModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio 10', ciudad='Santiago', pais='Chile')
        
    def test_laboratorio_data(self):
        laboratorio = Laboratorio.objects.get(pk=self.laboratorio.pk)
        self.assertEqual(laboratorio.nombre, 'Laboratorio 10')
        self.assertEqual(laboratorio.ciudad, 'Santiago')
        self.assertEqual(laboratorio.pais, 'Chile')

    def test_laboratorio_url(self):
        url = reverse('laboratorio:editar_laboratorio', args = [self.laboratorio.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_eliminar_laboratorio_template(self):
        url = reverse('laboratorio:eliminar_laboratorio', args = [self.laboratorio.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_laboratorios.html')



