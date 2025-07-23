from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializer import DrinkSerializer

@api_view(['GET'])
def listar_bebidas(request):
    bebidas = Drink.objects.all()
    serializer = DrinkSerializer(bebidas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_bebida(request):
    serializer = DrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_bebida(request, pk):
    try:
        bebida = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(bebida)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(bebida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bebida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)