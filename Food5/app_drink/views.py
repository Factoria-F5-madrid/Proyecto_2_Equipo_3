from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializer import DrinkSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def list_drink(request):
    drink = Drink.objects.all()
    serializer = DrinkSerializer(drink, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_drink(request):
    serializer = DrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_drink(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    serializer = DrinkSerializer(drink)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_drink(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    serializer = DrinkSerializer(drink, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_drink(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    drink.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)