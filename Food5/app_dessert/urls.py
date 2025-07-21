from django.urls import path
from . import views

urlpatterns = [
    path('desserts/', views.list_desserts, name='list_desserts'),
    path('desserts/create/', views.create_dessert, name='create_dessert'),
    path('desserts/<int:pk>/', views.detail_dessert, name='detail_dessert'),
    path('desserts/<int:pk>/edit/', views.edit_dessert, name='edit_dessert'),
    path('desserts/<int:pk>/delete/', views.delete_dessert, name='delete_dessert'),
]
