from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_drink, name='list_drink'),
    path('crear/', views.create_drink, name='create_drink'),
    path('<int:pk>/', views.detail_drink, name='detail_drink'),
]
