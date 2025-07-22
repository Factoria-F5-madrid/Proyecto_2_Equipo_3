from rest_framework import serializers
from .models import SecondCourse

# Serializer translates model instances to JSON and vice versa
class SecondCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondCourse
        fields = '__all__' # Include all fields from the SecondCourse model
        # Alternatively, you can specify fields explicitly:
        # fields = ['name', 'description', 'price', 'image', 'is_gluten_free', 'is_spicy', 'is_vegetarian']