from rest_framework import serializers
from .models import SecondCourse

# Serializer for SecondCourse model
class SecondCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondCourse
        fields = '__all__'  # Include all fields from the model
