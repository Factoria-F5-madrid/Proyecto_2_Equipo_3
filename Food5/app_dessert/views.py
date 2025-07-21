from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dessert
from .serializer import DessertSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def list_desserts(request):
    desserts = Dessert.objects.all()
    serializer = DessertSerializer(desserts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_dessert(request):
    serializer = DessertSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_dessert(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)
    serializer = DessertSerializer(dessert)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_dessert(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)
    serializer = DessertSerializer(dessert, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_dessert(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)
    dessert.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
