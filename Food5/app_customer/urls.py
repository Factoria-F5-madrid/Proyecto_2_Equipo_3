from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_customers, name='list_customers'),
    path('create', views.create_customer, name='create_customer'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
]