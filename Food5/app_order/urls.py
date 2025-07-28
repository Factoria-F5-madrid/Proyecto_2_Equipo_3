from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_orders, name='listar_orders'),
    path('create/', views.crear_order, name='crear_order'),
    path('<int:pk>/', views.detalle_order, name='detalle_order'),
    
    # NUEVAS URLs para el dashboard
    #path('dashboard/', views.dashboard_data, name='dashboard_data'),
    #path('by-date/', views.orders_by_date, name='orders_by_date'),
    #path('analytics/', views.menu_analytics, name='menu_analytics'),
    #path('customer/<int:customer_id>/', views.customer_orders, name='customer_orders'),
]