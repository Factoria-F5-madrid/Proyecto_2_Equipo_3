from django.test import TestCase
from .models import Dessert
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.urls import reverse

class DessertModelTest(TestCase):
    def test_create_dessert(self):
        # If you want to test image upload, use SimpleUploadedFile
        image = SimpleUploadedFile("tiramisu.jpg", b"file_content", content_type="image/jpeg")
        dessert = Dessert.objects.create(
            name="Tiramisú",
            calories=320,
            vegan=False,
            gluten_free=False,
            purchase_price=2.50,
            retail_price=5.00,
            picture=image  # or omit for no image
        )
        self.assertEqual(dessert.name, "Tiramisú")
        self.assertEqual(dessert.calories, 320)
        self.assertFalse(dessert.vegan)
        self.assertFalse(dessert.gluten_free)
        self.assertEqual(dessert.purchase_price, 2.50)
        self.assertEqual(dessert.retail_price, 5.00)
        self.assertIsNotNone(dessert.picture)

class DessertAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.image = SimpleUploadedFile("tiramisu.jpg", b"file_content", content_type="image/jpeg")
        self.dessert = Dessert.objects.create(
            name="Tiramisú",
            calories=320,
            vegan=False,
            gluten_free=False,
            purchase_price=2.50,
            retail_price=5.00,
            picture=self.image
        )

    def test_listar_postres(self):
        url = reverse('listar_postre')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(dessert['name'] == 'Tiramisú' for dessert in response.data))

    def test_crear_postre(self):
        url = reverse('crear_postre')
        #image = SimpleUploadedFile("flan.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'name': 'Flan de Vainilla',
            'calories': 250,
            'vegan': False,
            'gluten_free': True,
            'purchase_price': 1.80,
            'retail_price': 4.00,
            #'picture': image
        }
        response = self.client.post(url, data, format='multipart')
        #print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Flan de Vainilla')

    def test_detalle_postre_get(self):
        url = reverse('detalle_postre', args=[self.dessert.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Tiramisú')

    def test_detalle_postre_put(self):
        url = reverse('detalle_postre', args=[self.dessert.pk])
        data = {
            'name': 'Tiramisú Actualizado',
            'calories': 340,
            'vegan': True,
            'gluten_free': True,
            'retail_price': 5.50,
            #'picture': self.image
        }
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Tiramisú Actualizado')

    def test_detalle_postre_delete(self):
        url = reverse('detalle_postre', args=[self.dessert.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Dessert.objects.filter(pk=self.dessert.pk).exists())

from .serializer import DessertSerializer

class DessertSerializerTest(TestCase):
    def test_serializer_validation(self):
        data = {
            'name': 'Cheesecake de Frutos Rojos',
            'calories': 380,
            'vegan': False,
            'gluten_free': False,
            'retail_price': 6.50,
            'picture': None
        }
        serializer = DessertSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)