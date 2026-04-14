from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from auth_management_system.helper.auth_mamagement_system_helper_class import validate_user_login
from auth_management_system.helper.model_class import UsersRequest
from common.common_class.util import build_request_with_user

class LoginServiceAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-11 05:20 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle login_service_api insert operations
    """

    def post(self, request):
        try:
            record = build_request_with_user(UsersRequest, request, method='POST')

            result = validate_user_login(record)

            return JsonResponse(result)

        except ValidationError as e:
            return JsonResponse(
                {"status": "failed", "errors": e.errors()},
                status=400
            )

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-11 05:20 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle login_service_api get operations
    """

    def get(self, request):
        # Your logic here
        return Response({})        

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-11 05:20 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle login_service_api update operations
    """

    def put(self, request):
        # Your logic here
        return Response({})
        
    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-11 05:20 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle login_service_api delete operations
    """

    def delete(self, request):
        # Your logic here
        return Response({})
