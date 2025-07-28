# appa_user/serializers.py
from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'password']

    def create(self, validated_data):
        return Usuario.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            nombre=validated_data.get('nombre', '')
        )

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Credenciales inválidas.")
        return {'user': user}