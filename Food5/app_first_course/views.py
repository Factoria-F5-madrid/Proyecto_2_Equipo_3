from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FirstCourse
from .serializer import FirstCourseSerializer

@api_view(['GET'])
def listar_platos(request):
    platos = FirstCourse.objects.all()
    serializer = FirstCourseSerializer(platos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_plato(request):
    serializer = FirstCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_plato(request, pk):
    try:
        plato = FirstCourse.objects.get(pk=pk)
    except FirstCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FirstCourseSerializer(plato)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FirstCourseSerializer(plato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
