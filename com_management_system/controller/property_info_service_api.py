from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from com_management_system.helper.com_management_system_helper_class import get_com_properties, insert_com_property
from com_management_system.helper.model_class import PropertiesRequest
from common.common_class.util import build_request_with_user

class PropertyInfoServiceAPIView(APIView):
    permission_classes = [AllowAny]  # Adjust permissions as needed

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 04:15 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_info_service_api insert operations
    """

    def post(self, request):
        try:
            record = build_request_with_user(PropertiesRequest, request, method='POST')

            result = insert_com_property(record)

            return JsonResponse(result)

        except ValidationError as e:
            return JsonResponse(
                {"status": "failed", "errors": e.errors()},
                status=400
            )  

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 04:15 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_info_service_api get operations
    """

    def get(self, request):
        try:
            record = build_request_with_user(PropertiesRequest, request, method='GET')

            result = get_com_properties(record)

            return JsonResponse(result)

        except ValidationError as e:
            return JsonResponse(
                {"status": "failed", "errors": e.errors()},
                status=400
            )        

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 04:15 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_info_service_api update operations
    """

    def put(self, request):
        # Your logic here
        return Response({})
        
    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 04:15 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle property_info_service_api delete operations
    """

    def delete(self, request):
        # Your logic here
        return Response({})
