from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from auth_management_system.helper.auth_mamagement_system_helper_class import logout_user

class LogoutServiceAPIView(APIView):
    permission_classes = [AllowAny]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 01:16 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle logout_service_api insert operations
    """

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")

            if not refresh_token:
                return JsonResponse(
                    Response("failed", "refresh_token is required"),
                    status=400
                )

            result = logout_user(refresh_token)

            status_code = 200 if result.get("status") == "success" else 400

            return JsonResponse(result, status=status_code)

        except Exception as ex:
            return JsonResponse(
                Response("error", str(ex)),
                status=500
            )

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 01:16 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle logout_service_api get operations
    """

    def get(self, request):
        # Your logic here
        return Response({})        

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 01:16 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle logout_service_api update operations
    """

    def put(self, request):
        # Your logic here
        return Response({})
        
    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 01:16 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle logout_service_api delete operations
    """

    def delete(self, request):
        # Your logic here
        return Response({})
