# app_dessert/serializers.py
from rest_framework import serializers
from .models import Dessert

class DessertSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dessert
        fields = [
            'name',
            'calories',
            'vegan',
            'gluten_free',
            'purchase_price',
            'retail_price',
            'picture',
        ]


