# user_management_system/urls.py
from django.urls import path

from com_management_system.controller.property_diagnosis_report_service_api import PropertyDiagnosisReportServiceAPIView
from com_management_system.controller.property_info_service_api import PropertyInfoServiceAPIView
from com_management_system.controller.property_monthly_config_service_api import PropertyMonthlyConfigServiceAPIView
from com_management_system.controller.property_performance_report_service_api import PropertyPerformanceReportServiceAPIView
from com_management_system.controller.property_performance_service_api import PropertyPerformanceServiceAPIView
urlpatterns = [
      
    path('property-diagnosis-report-service/', PropertyDiagnosisReportServiceAPIView.as_view(), name='property-diagnosis-report-service'),
    path('property-performance-report-service/', PropertyPerformanceReportServiceAPIView.as_view(), name='property-performance-report-service'),
    path('property-performance-service/', PropertyPerformanceServiceAPIView.as_view(), name='property-performance-service'),
    path('property-monthly-config-service/', PropertyMonthlyConfigServiceAPIView.as_view(), name='property-monthly-config-service'),
    path('property-info-service/', PropertyInfoServiceAPIView.as_view(), name='property-info-service'),
]
