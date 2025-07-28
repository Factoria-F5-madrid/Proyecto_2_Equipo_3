from django.test import TestCase
from .models import Bread
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.urls import reverse

class BreadModelTest(TestCase):
    def test_create_bread(self):
        # If you want to test image upload, use SimpleUploadedFile
        image = SimpleUploadedFile("pan_integral.jpg", b"file_content", content_type="image/jpeg")
        bread = Bread.objects.create(
            name="Pan Integral",
            calories=120,
            vegan=True,
            gluten_free=False,
            purchase_price=1.50,
            retail_price=3.00,
            picture=image  # or omit for no image
        )
        self.assertEqual(bread.name, "Pan Integral")
        self.assertEqual(bread.calories, 120)
        self.assertTrue(bread.vegan)
        self.assertFalse(bread.gluten_free)
        self.assertEqual(bread.purchase_price, 1.50)
        self.assertEqual(bread.retail_price, 3.00)
        self.assertIsNotNone(bread.picture)

class BreadAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.image = SimpleUploadedFile("pan_integral.jpg", b"file_content", content_type="image/jpeg")
        self.bread = Bread.objects.create(
            name="Pan Integral",
            calories=120,
            vegan=True,
            gluten_free=False,
            purchase_price=1.50,
            retail_price=3.00,
            picture=self.image
        )

    def test_listar_panes(self):
        url = reverse('listar_pan')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(bread['name'] == 'Pan Integral' for bread in response.data))

    def test_crear_pan(self):
        url = reverse('crear_pan')
        #image = SimpleUploadedFile("pan_blanco.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'name': 'Pan Blanco',
            'calories': 100,
            'vegan': False,
            'gluten_free': False,
            'purchase_price': 1.20,
            'retail_price': 2.50,
            #'picture': image
        }
        response = self.client.post(url, data, format='multipart')
        #print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Pan Blanco')

    def test_detalle_pan_get(self):
        url = reverse('detalle_pan', args=[self.bread.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Pan Integral')

    def test_detalle_pan_put(self):
        url = reverse('detalle_pan', args=[self.bread.pk])
        data = {
            'name': 'Pan Integral Actualizado',
            'calories': 130,
            'vegan': False,
            'gluten_free': True,
            'retail_price': 3.50,
            #'picture': self.image
        }
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Pan Integral Actualizado')

    def test_detalle_pan_delete(self):
        url = reverse('detalle_pan', args=[self.bread.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Bread.objects.filter(pk=self.bread.pk).exists())

from .serializers import BreadSerializer

class BreadSerializerTest(TestCase):
    def test_serializer_validation(self):
        data = {
            'name': 'Pan de Centeno',
            'calories': 140,
            'vegan': True,
            'gluten_free': False,
            'retail_price': 3.20,
            'picture': None
        }
        serializer = BreadSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
