from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = [
            'name',
            'calories',
            'vegan',
            'gluten_free',
            'purchase_price',
            'retail_price',
            'picture',
        ]
    