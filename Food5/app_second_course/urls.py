from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_second_course, name='list_second_course'),
    path('create/', views.create_second_course, name='create_second_course'),
    path('<int:pk>/', views.detail_second_course, name='detail_second_course'),
]