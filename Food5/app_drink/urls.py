from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_bebidas, name='listar_bebidas'),
    path('create/', views.crear_bebida, name='crear_bebida'),
    path('<int:pk>/', views.detalle_bebida, name='detalle_bebida'),
]