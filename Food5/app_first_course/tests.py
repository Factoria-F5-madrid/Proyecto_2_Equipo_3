from django.test import TestCase
from .models import FirstCourse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.urls import reverse

class FirstCourseModelTest(TestCase):
    def test_create_first_course(self):
        # If you want to test image upload, use SimpleUploadedFile
        image = SimpleUploadedFile("crema-de-calabaza-1.jpg", b"file_content", content_type="image/jpeg")
        fc = FirstCourse.objects.create(
            name="crema-de-calabaza",
            calories=150,
            vegan=True,
            gluten_free=True,
            purchase_price=2.50,
            retail_price=5.00,
            picture=image  # or omit for no image
        )
        self.assertEqual(fc.name, "crema-de-calabaza")
        self.assertEqual(fc.calories, 150)
        self.assertTrue(fc.vegan)
        self.assertTrue(fc.gluten_free)
        self.assertEqual(fc.purchase_price, 2.50)
        self.assertEqual(fc.retail_price, 5.00)
        self.assertIsNotNone(fc.picture)

class FirstCourseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.image = SimpleUploadedFile("crema-de-calabaza-1.jpg", b"file_content", content_type="image/jpeg")
        self.first_course = FirstCourse.objects.create(
            name="crema-de-calabaza",
            calories=150,
            vegan=True,
            gluten_free=True,
            purchase_price=2.50,
            retail_price=5.00,
            picture=self.image
        )

    def test_listar_platos(self):
        url = reverse('listar_platos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(fc['name'] == 'crema-de-calabaza' for fc in response.data))

    def test_crear_plato(self):
        url = reverse('crear_plato')
        #image = SimpleUploadedFile("crema-de-calabaza-1.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'name': 'sopa de tomate',
            'calories': 120,
            'vegan': False,
            'gluten_free': True,
            'purchase_price': 2.50,
            'retail_price': 4.00,
            #'picture': image
        }
        response = self.client.post(url, data, format='multipart')
        #print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'sopa de tomate')

    def test_detalle_plato_get(self):
        url = reverse('detalle_plato', args=[self.first_course.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'crema-de-calabaza')

    def test_detalle_plato_put(self):
        url = reverse('detalle_plato', args=[self.first_course.pk])
        data = {
            'name': 'crema actualizada',
            'calories': 160,
            'vegan': False,
            'gluten_free': False,
            'retail_price': 6.00,
            #'picture': self.image
        }
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'crema actualizada')

    def test_detalle_plato_delete(self):
        url = reverse('detalle_plato', args=[self.first_course.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(FirstCourse.objects.filter(pk=self.first_course.pk).exists())

from .serializers import FirstCourseSerializer

class FirstCourseSerializerTest(TestCase):
    def test_serializer_validation(self):
        data = {
            'name': 'gazpacho',
            'calories': 90,
            'vegan': True,
            'gluten_free': True,
            'retail_price': 3.50,
            'picture': None
        }
        serializer = FirstCourseSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
