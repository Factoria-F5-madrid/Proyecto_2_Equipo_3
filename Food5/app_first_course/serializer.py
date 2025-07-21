# first_course/serializers.py

from rest_framework import serializers
from .models import FirstCourse

class FirstCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstCourse
        fields = ['name', 'calories', 'vegan', 'gluten_free', 'retail_price', 'picture']
