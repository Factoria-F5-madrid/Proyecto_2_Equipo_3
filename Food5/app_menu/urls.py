from django.urls import path
from .views import listar_menus, crear_menu, detalle_menu

urlpatterns = [
    path('', listar_menus, name='listar_menus'),
    path('create/', crear_menu, name='crear_menus'),
    path('<int:pk>/', detalle_menu, name='detallar_menus'),
]