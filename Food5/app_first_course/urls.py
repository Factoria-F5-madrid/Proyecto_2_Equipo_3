from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_platos, name='listar_platos'),
    path('crear/', views.crear_plato, name='crear_plato'),
    path('<int:pk>/', views.detalle_plato, name='detalle_plato'),
]
