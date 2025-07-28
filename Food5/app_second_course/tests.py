from django.test import TestCase
from .models import SecondCourse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.urls import reverse

class SecondCourseModelTest(TestCase):
    def test_create_second_course(self):
        # If you want to test image upload, use SimpleUploadedFile
        image = SimpleUploadedFile("paella.jpg", b"file_content", content_type="image/jpeg")
        second_course = SecondCourse.objects.create(
            name="Paella Valenciana",
            calories=450,
            vegan=False,
            gluten_free=True,
            purchase_price=8.50,
            retail_price=18.00,
            picture=image  # or omit for no image
        )
        self.assertEqual(second_course.name, "Paella Valenciana")
        self.assertEqual(second_course.calories, 450)
        self.assertFalse(second_course.vegan)
        self.assertTrue(second_course.gluten_free)
        self.assertEqual(second_course.purchase_price, 8.50)
        self.assertEqual(second_course.retail_price, 18.00)
        self.assertIsNotNone(second_course.picture)

class SecondCourseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.image = SimpleUploadedFile("paella.jpg", b"file_content", content_type="image/jpeg")
        self.second_course = SecondCourse.objects.create(
            name="Paella Valenciana",
            calories=450,
            vegan=False,
            gluten_free=True,
            purchase_price=8.50,
            retail_price=18.00,
            picture=self.image
        )

    def test_listar_segundos(self):
        url = reverse('list_second_course')  # Changed to match actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(second_course['name'] == 'Paella Valenciana' for second_course in response.data))

    def test_crear_segundo(self):
        url = reverse('create_second_course')  # Changed to match actual URL name
        #image = SimpleUploadedFile("lasagna.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'name': 'Lasaña Boloñesa',
            'calories': 380,
            'vegan': False,
            'gluten_free': False,
            'purchase_price': 6.50,
            'retail_price': 15.00,
            #'picture': image
        }
        response = self.client.post(url, data, format='multipart')
        #print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Lasaña Boloñesa')

    def test_detalle_segundo_get(self):
        url = reverse('detail_second_course', args=[self.second_course.pk])  # Changed to match actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Paella Valenciana')

    def test_detalle_segundo_put(self):
        url = reverse('detail_second_course', args=[self.second_course.pk])  # Changed to match actual URL name
        data = {
            'name': 'Paella de Verduras',
            'calories': 380,
            'vegan': True,
            'gluten_free': True,
            'retail_price': 16.00,
            #'picture': self.image
        }
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Paella de Verduras')

    def test_detalle_segundo_delete(self):
        url = reverse('detail_second_course', args=[self.second_course.pk])  # Changed to match actual URL name
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(SecondCourse.objects.filter(pk=self.second_course.pk).exists())

from .serializers import SecondCourseSerializer

class SecondCourseSerializerTest(TestCase):
    def test_serializer_validation(self):
        data = {
            'name': 'Arroz con Pollo',
            'calories': 420,
            'vegan': False,
            'gluten_free': True,
            'retail_price': 14.50,
            'picture': None
        }
        serializer = SecondCourseSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)