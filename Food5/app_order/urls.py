from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_orders, name='listar_orders'),
    path('create/', views.crear_order, name='crear_order'),
    path('<int:pk>/', views.detalle_order, name='detalle_order'),
]