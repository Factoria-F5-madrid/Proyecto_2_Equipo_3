from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_postres, name='listar_postre'),
    path('crear/', views.crear_postre, name='crear_postre'),
    path('<int:pk>/', views.detalle_postre, name='detalle_postre'),
]