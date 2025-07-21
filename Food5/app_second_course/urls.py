from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SecondCourseViewSet

# ✅ Router automatically creates URLs for your ViewSet
router = DefaultRouter()
router.register(r'second-courses', SecondCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include router-generated URLs
]