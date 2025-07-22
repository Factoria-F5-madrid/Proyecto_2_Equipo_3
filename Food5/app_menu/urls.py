from django.urls import path
from .views import listar_menus, crear_menu, detalle_menu

urlpatterns = [
    path('menus/', listar_menus),
    path('menus/create/', crear_menu),
    path('menus/<int:pk>/', detalle_menu),
]