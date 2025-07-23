from rest_framework import generics
from app_customer.models import Customer
from .serializers import CustomerSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer