from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import pandas as pd
import json

from migration_management_system.helper.migration_management_system_helper_class import insert_mgn_performance_uploads
class PerformanceUploadsServiceAPIView(APIView):
    permission_classes = [AllowAny]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 03:04 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle mgn_performance_uploads_service_api insert operations
    """

    def post(self, request):

        try:
            print('API hit')

            # 1. Get file from the request
            excel_file = request.FILES.get('file')
            if not excel_file:
                return JsonResponse(
                    {"status": "failed", "message": "No file uploaded"},
                    status=400
                )

            # 2. Get user-provided parameters from request
            company_id = request.data.get('company_id')
            property_id = request.data.get('property_id')
            uploaded_by = request.data.get('uploaded_by')
            upload_month = request.data.get('upload_month')
            upload_year = request.data.get('upload_year')

            if not all([company_id, property_id, uploaded_by, upload_month, upload_year]):
                return JsonResponse(
                    {"status": "failed", "message": "Missing required parameters"},
                    status=400
                )

            # 3. Extract the file name from the uploaded file
            file_name = excel_file.name

            # 4. Read the Excel file (ensure data is safe to process)
            df = pd.read_excel(excel_file)

            # 5. Force all columns to string to prevent type issues
            df = df.astype(str)

            # 6. Replace pandas NaN values with None (so JSON is clean)
            df = df.where(pd.notnull(df), None)

            # 7. Convert DataFrame to JSON array
            data_json = df.to_json(orient="records")

            # 8. Call the migration function to insert the data into the database
            result = insert_mgn_performance_uploads(df, company_id, property_id, uploaded_by, file_name, upload_month, upload_year)

            return JsonResponse(result)

        except Exception as ex:
            return JsonResponse({"status": "error", "message": str(ex)}, status=500)

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 03:04 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle mgn_performance_uploads_service_api get operations
    """

    def get(self, request):
        # Your logic here
        return Response({})        

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 03:04 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle mgn_performance_uploads_service_api update operations
    """

    def put(self, request):
        # Your logic here
        return Response({})
        
    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 2026-04-13 03:04 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to handle mgn_performance_uploads_service_api delete operations
    """

    def delete(self, request):
        # Your logic here
        return Response({})
