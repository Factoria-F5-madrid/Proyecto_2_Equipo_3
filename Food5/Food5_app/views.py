from rest_framework import viewsets
from .models import SecondCourse
from .serializers import SecondCourseSerializer

# ViewSet provides CRUD operations (list, create, retrieve, update, delete)
class SecondCourseViewSet(viewsets.ModelViewSet):
    queryset = SecondCourse.objects.all()  # All SecondCourse entries from the database
    serializer_class = SecondCourseSerializer  # Use the defined serializer
