from django.urls import path
from .views import exportAllToCsv  # adjust import based on location

urlpatterns = [
    path('export/csv/', exportAllToCsv, name='export_csv'),
]
