from django.test import TestCase
from .models import Drink
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.urls import reverse

class DrinkModelTest(TestCase):
    def test_create_drink(self):
        # If you want to test image upload, use SimpleUploadedFile
        image = SimpleUploadedFile("coca_cola.jpg", b"file_content", content_type="image/jpeg")
        drink = Drink.objects.create(
            name="Coca Cola",
            calories=140,
            vegan=True,
            gluten_free=True,
            purchase_price=0.80,
            retail_price=2.00,
            picture=image  # or omit for no image
        )
        self.assertEqual(drink.name, "Coca Cola")
        self.assertEqual(drink.calories, 140)
        self.assertTrue(drink.vegan)
        self.assertTrue(drink.gluten_free)
        self.assertEqual(drink.purchase_price, 0.80)
        self.assertEqual(drink.retail_price, 2.00)
        self.assertIsNotNone(drink.picture)

class DrinkAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.image = SimpleUploadedFile("coca_cola.jpg", b"file_content", content_type="image/jpeg")
        self.drink = Drink.objects.create(
            name="Coca Cola",
            calories=140,
            vegan=True,
            gluten_free=True,
            purchase_price=0.80,
            retail_price=2.00,
            picture=self.image
        )

    def test_list_drinks(self):
        url = reverse('listar_bebidas')  # Changed to match actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(drink['name'] == 'Coca Cola' for drink in response.data))

    def test_create_drink(self):
        url = reverse('crear_bebida')  # Changed to match actual URL name
        #image = SimpleUploadedFile("agua.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'name': 'Agua Mineral',
            'calories': 0,
            'vegan': True,
            'gluten_free': True,
            'purchase_price': 0.30,
            'retail_price': 1.50,
            #'picture': image
        }
        response = self.client.post(url, data, format='multipart')
        #print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Agua Mineral')

    def test_detail_drink_get(self):
        url = reverse('detalle_bebida', args=[self.drink.pk])  # Changed to match actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Coca Cola')

    def test_detail_drink_put(self):
        url = reverse('detalle_bebida', args=[self.drink.pk])  # Changed to match actual URL name
        data = {
            'name': 'Coca Cola Zero',
            'calories': 0,
            'vegan': True,
            'gluten_free': True,
            'retail_price': 2.20,
            #'picture': self.image
        }
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Coca Cola Zero')

    def test_detail_drink_delete(self):
        url = reverse('detalle_bebida', args=[self.drink.pk])  # Changed to match actual URL name
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Drink.objects.filter(pk=self.drink.pk).exists())

from .serializers import DrinkSerializer

class DrinkSerializerTest(TestCase):
    def test_serializer_validation(self):
        data = {
            'name': 'Zumo de Naranja',
            'calories': 110,
            'vegan': True,
            'gluten_free': True,
            'retail_price': 3.50,
            'picture': None
        }
        serializers = DrinkSerializer(data=data)
        self.assertTrue(serializers.is_valid(), serializers.errors)