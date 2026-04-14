# user_management_system/urls.py
from django.urls import path

from migration_management_system.controller.performance_uploads_service_api import PerformanceUploadsServiceAPIView

urlpatterns = [
      
    path('performance-uploads-service/', PerformanceUploadsServiceAPIView.as_view(), name='performance-uploads-service'),
]
