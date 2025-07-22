from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dessert
from .serializer import DessertSerializer

@api_view(['GET'])
def listar_postres(request):
    postres = Dessert.objects.all()
    serializer = DessertSerializer(postres, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_postre(request):
    serializer = DessertSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_postre(request, pk):
    try:
        postre = Dessert.objects.get(pk=pk)
    except Dessert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DessertSerializer(postre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DessertSerializer(postre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        postre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)