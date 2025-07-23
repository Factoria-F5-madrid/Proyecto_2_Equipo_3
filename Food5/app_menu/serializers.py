from rest_framework import serializers
from .models import Menu
from app_first_course.serializer import FirstCourseSerializer
from app_second_course.serializers import SecondCourseSerializer
from app_dessert.serializer import DessertSerializer
from app_drink.serializer import DrinkSerializer
from app_Bread.serializer import BreadSerializer
from app_first_course.models import FirstCourse
from app_second_course.models import SecondCourse
from app_dessert.models import Dessert
from app_drink.models import Drink
from app_Bread.models import Bread

class MenuSerializer(serializers.ModelSerializer):
    # Campos de solo lectura para mostrar detalles anidados
    first_course = FirstCourseSerializer(read_only=True)
    second_course = SecondCourseSerializer(read_only=True)
    dessert = DessertSerializer(read_only=True)
    drink = DrinkSerializer(read_only=True)
    bread = BreadSerializer(read_only=True)

    # Campos de solo escritura para aceptar IDs
    first_course_id = serializers.PrimaryKeyRelatedField(
        queryset=FirstCourse.objects.all(), source='first_course', write_only=True
    )
    second_course_id = serializers.PrimaryKeyRelatedField(
        queryset=SecondCourse.objects.all(), source='second_course', write_only=True
    )
    dessert_id = serializers.PrimaryKeyRelatedField(
        queryset=Dessert.objects.all(), source='dessert', write_only=True
    )
    drink_id = serializers.PrimaryKeyRelatedField(
        queryset=Drink.objects.all(), source='drink', write_only=True
    )
    bread_id = serializers.PrimaryKeyRelatedField(
        queryset=Bread.objects.all(), source='bread', write_only=True
    )

    class Meta:
        model = Menu
        fields = [
            'id',
            'first_course', 'first_course_id',
            'second_course', 'second_course_id',
            'dessert', 'dessert_id',
            'drink', 'drink_id',
            'bread', 'bread_id',
            'purchase_price',
            'retail_price'
        ]