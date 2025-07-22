from django.urls import path
from . import views

urlpatterns = [
    path('drink/', views.list_drink, name='list_drink'),
    path('drink/create/', views.create_drink, name='create_drink'),
    path('drink/<int:pk>/', views.detail_drink, name='detail_drink'),
    path('drink/<int:pk>/edit/', views.edit_drink, name='edit_drink'),
    path('drink/<int:pk>/delete/', views.delete_drink, name='delete_drink'),
]
