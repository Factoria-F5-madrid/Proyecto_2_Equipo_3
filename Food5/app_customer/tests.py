from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Customer
from .serializers import CustomerSerializer

class CustomerModelTest(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(
            name="Juan Pérez",
            email="juan.perez@email.com",
            address="Calle Mayor 123, Madrid"
        )
        self.assertEqual(customer.name, "Juan Pérez")
        self.assertEqual(customer.email, "juan.perez@email.com")
        self.assertEqual(customer.address, "Calle Mayor 123, Madrid")
        # Updated to match the new __str__ method format
        self.assertEqual(str(customer), "Juan Pérez - juan.perez@email.com - Calle Mayor 123, Madrid")

    def test_customer_email_unique(self):
        Customer.objects.create(
            name="Juan Pérez",
            email="juan.perez@email.com",
            address="Calle Mayor 123, Madrid"
        )
        # Test that creating another customer with same email raises an error
        with self.assertRaises(Exception):
            Customer.objects.create(
                name="María García",
                email="juan.perez@email.com",  # Same email
                address="Calle Menor 456, Barcelona"
            )

class CustomerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            name="Juan Pérez",
            email="juan.perez@email.com",
            address="Calle Mayor 123, Madrid"
        )

    def test_list_customers(self):
        url = reverse('list_customers')  # Adjust URL name as needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(customer['name'] == 'Juan Pérez' for customer in response.data))

    def test_create_customer(self):
        url = reverse('create_customer')  # Adjust URL name as needed
        data = {
            'name': 'María García',
            'email': 'maria.garcia@email.com',
            'address': 'Calle Menor 456, Barcelona'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'María García')

    def test_detail_customer_get(self):
        url = reverse('customer_detail', args=[self.customer.pk])  # Adjust URL name as needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Juan Pérez')

    def test_detail_customer_put(self):
        url = reverse('customer_detail', args=[self.customer.pk])  # Adjust URL name as needed
        data = {
            'name': 'Juan Carlos Pérez',
            'email': 'juan.carlos@email.com',
            'address': 'Avenida Central 789, Valencia'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Juan Carlos Pérez')

    def test_detail_customer_delete(self):
        url = reverse('customer_detail', args=[self.customer.pk])  # Adjust URL name as needed
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Customer.objects.filter(pk=self.customer.pk).exists())

class CustomerSerializerTest(TestCase):
    def test_serializer_validation(self):
        data = {
            'name': 'Ana López',
            'email': 'ana.lopez@email.com',
            'address': 'Plaza España 321, Sevilla'
        }
        serializer = CustomerSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_serializer_invalid_email(self):
        data = {
            'name': 'Ana López',
            'email': 'invalid-email',  # Invalid email format
            'address': 'Plaza España 321, Sevilla'
        }
        serializer = CustomerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
