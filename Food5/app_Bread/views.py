from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bread
from .serializer import BreadSerializer

@api_view(['GET'])
def listar_panes(request):
    panes = Bread.objects.all()
    serializer = BreadSerializer(panes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_pan(request):
    serializer = BreadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_pan(request, pk):
    try:
        pan = Bread.objects.get(pk=pk)
    except Bread.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BreadSerializer(pan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BreadSerializer(pan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
