# app_order/serializers.py

from rest_framework import serializers
from .models import Order
from app_menu.models import Menu
from app_customer.models import Customer
from app_menu.serializers import MenuSerializer
from app_customer.serializers import CustomerSerializer

class OrderSerializer(serializers.ModelSerializer):
    # Lectura (detalles anidados)
    menus = MenuSerializer(many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)

    # Escritura (enviar IDs)
    menu_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Menu.objects.all(), write_only=True, source='menus'
    )
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), write_only=True, source='customer'
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'menus', 'menu_ids',
            'customer', 'customer_id',
            'due_date',
            'gotten_date',
            'purchase_price',
            'retail_price'
        ]