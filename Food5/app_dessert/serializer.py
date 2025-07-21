# app_dessert/serializers.py
from rest_framework import serializers
from .models import Dessert

class DessertSerializer(serializers.ModelSerializer):
    picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Dessert
        fields = [
            'id',
            'name',
            'calories',
            'vegan',
            'gluten_free',
            'purchase_price',
            'retail_price',
            'picture',
            'picture_url',
        ]

    def get_picture_url(self, obj):
        if obj.picture:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.picture.url) if request else obj.picture.url
        return None

    def create(self, validated_data):
        return Dessert.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
