from django.test import TestCase
from django.urls import reverse
from .models import Categoria


class CategoriaTests(TestCase):
	def test_listado_muestra_formulario_y_categorias(self):
		Categoria.objects.create(nombre='Bebidas')

		response = self.client.get(reverse('listar_categorias'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Registrar categoría')
		self.assertContains(response, 'Bebidas')

	def test_post_registra_categoria_y_redirige_al_listado(self):
		response = self.client.post(
			reverse('listar_categorias'),
			{'nombre': '  Bebidas  ', 'observacion': '  Frías  '},
		)

		self.assertRedirects(response, reverse('listar_categorias'))
		categoria = Categoria.objects.get(nombre='Bebidas')
		self.assertEqual(categoria.observacion, 'Frías')
