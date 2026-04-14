from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from com_management_system.helper.com_management_system_helper_class import get_com_property_monthly_performance
from com_management_system.helper.model_class import PropertyDiagnosisRequest
from common.common_class.util import build_request_with_user

class PropertyPerformanceReportServiceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 02:35 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_performance_service_api insert operations
    """

    def post(self, request):
        # Your logic here
        return Response({})

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 02:35 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_performance_service_api get operations
    """

    def get(self, request):
        try:
            record = build_request_with_user(PropertyDiagnosisRequest, request, method='GET')

            result = get_com_property_monthly_performance(record)

            return JsonResponse(result)

        except ValidationError as e:
            return JsonResponse(
                {"status": "failed", "errors": e.errors()},
                status=400
            )           

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 02:35 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_performance_service_api update operations
    """

    def put(self, request):
        # Your logic here
        return Response({})
        
    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 02:35 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_performance_service_api delete operations
    """

    def delete(self, request):
        # Your logic here
        return Response({})
