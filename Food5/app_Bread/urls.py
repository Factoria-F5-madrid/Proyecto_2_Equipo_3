from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_panes, name='listar_pan'),
    path('crear/', views.crear_pan, name='crear_pan'),
    path('<int:pk>/', views.detalle_pan, name='detalle_pan'),
]