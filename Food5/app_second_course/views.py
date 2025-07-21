from django.shortcuts import render
from rest_framework import viewsets
from .models import SecondCourse
from .serializers import SecondCourseSerializer

# Create your views here.
# ViewSet for SecondCourse model
class SecondCourseViewSet(viewsets.ModelViewSet):
    queryset = SecondCourse.objects.all() # Get all SecondCourse objects
    serializer_class = SecondCourseSerializer # Use the SecondCourseSerializer to serialize the data