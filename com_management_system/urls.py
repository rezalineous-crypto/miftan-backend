# user_management_system/urls.py
from django.urls import path

from auth_management_system.controller.login_service_api import LoginServiceAPIView
from auth_management_system.controller.logout_service_api import LogoutServiceAPIView
from auth_management_system.controller.refresh_token_service_api import RefreshTokenServiceAPIView
from auth_management_system.controller.users_service_api import UsersServiceAPIView
from com_management_system.controller.property_diagnosis_report_service_api import PropertyDiagnosisReportServiceAPIView
from com_management_system.controller.property_performance_report_service_api import PropertyPerformanceReportServiceAPIView
from com_management_system.controller.property_performance_service_api import PropertyPerformanceServiceAPIView
urlpatterns = [
      
    path('property-diagnosis-report-service/', PropertyDiagnosisReportServiceAPIView.as_view(), name='property-diagnosis-report-service'),
    path('property-performance-report-service/', PropertyPerformanceReportServiceAPIView.as_view(), name='property-performance-report-service'),
    path('property-performance-service/', PropertyPerformanceServiceAPIView.as_view(), name='property-performance-service'),
    #path('performance-uploads-service/', PerformanceUploadsServiceAPIView.as_view(), name='performance-uploads-service'),
]
