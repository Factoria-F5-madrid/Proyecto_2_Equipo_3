from django.urls import path
from .views import listar_menus, crear_menu, detalle_menu

urlpatterns = [
    path('', listar_menus),
    path('create/', crear_menu),
    path('<int:pk>/', detalle_menu),
]