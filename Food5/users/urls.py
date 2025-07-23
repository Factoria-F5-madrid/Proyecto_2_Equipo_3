# users/urls.py

from django.urls import path
from .views import RegisterView  # Asegúrate de que ya tienes esta vista creada

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]