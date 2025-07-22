from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SecondCourse
from .serializers import SecondCourseSerializer

@api_view(['GET'])
def list_second_course(request):
    segundos = SecondCourse.objects.all()
    serializer = SecondCourseSerializer(segundos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_second_course(request):
    serializer = SecondCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_second_course(request, pk):
    try:
        segundo = SecondCourse.objects.get(pk=pk)
    except SecondCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SecondCourseSerializer(segundo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SecondCourseSerializer(segundo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        segundo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)