from rest_framework import viewsets
from .models import Dessert
from .serializer import DessertSerializer

class DessertViewSet(viewsets.ModelViewSet):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
