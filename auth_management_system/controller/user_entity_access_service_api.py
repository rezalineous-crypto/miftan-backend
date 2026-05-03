from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from auth_management_system.helper.auth_mamagement_system_helper_class import get_auth_user_entity_access, insert_user_entity_access
from auth_management_system.helper.model_class import UserEntityAccessRequest
# from util import build_request_with_user

class UserEntityAccessServiceAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-05-01
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle user_entity_access_service_api insert operations
    """

    def post(self, request):
        try:
            record = build_request_with_user(UserEntityAccessRequest, request, method='POST')

            result = insert_user_entity_access(record)

            return JsonResponse(result)

        except ValidationError as e:
            return JsonResponse(
                {"status": "failed", "errors": e.errors()},
                status=400
            )   

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-05-01
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle user_entity_access_service_api get operations
    """

    def get(self, request):
        try:
            record = build_request_with_user(UserEntityAccessRequest, request, method='GET')

            result = get_auth_user_entity_access(record)

            return JsonResponse(result)

        except ValidationError as e:
            return JsonResponse(
                {"status": "failed", "errors": e.errors()},
                status=400
            )   
      

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-05-01
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle user_entity_access_service_api update operations
    """

    def put(self, request):
        # Your logic here
        return Response({})
        
    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-05-01
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle user_entity_access_service_api delete operations
    """

    def delete(self, request):
        # Your logic here
        return Response({})
