# app_dessert/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DessertViewSet

router = DefaultRouter()
router.register(r'desserts', DessertViewSet, basename='dessert')

urlpatterns = [
    path('', include(router.urls)),
]
