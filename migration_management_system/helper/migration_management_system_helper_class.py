import json

from common.common_class.db import call_db_function, get_db_connection
from common.common_class.util import _response
from migration_management_system.helper.model_class import PerformanceUploadsRequest
'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for getting asset list from DB
'''
def insert_mgn_performance_uploads(df, company_id, property_id, uploaded_by, file_name, upload_month, upload_year):
    try:
        with get_db_connection() as conn:
            # 1. Convert DataFrame to JSON (records format)
            data_json = df.to_json(orient="records")
            
            # 2. Create the full data payload for the PostgreSQL function
            p_data = {
                "company_id": company_id,
                "property_id": property_id,
                "uploaded_by": uploaded_by,
                "file_name": file_name,
                "upload_month": upload_month,
                "upload_year": upload_year,
                "data": json.loads(data_json)  # This will be the actual data from the Excel
            }
            print (json.loads(data_json))
            # 3. Call the PostgreSQL function with the prepared data
            rows = call_db_function(conn, "public.fn_insert_mgn_performance_uploads", [json.dumps(p_data)])
            
            if not rows:
                return _response("failed", "Error Occurred While Processing Request")
            
            # 4. Handle the PostgreSQL response
            result = rows[0]  # Assuming it returns a result object with status and message

            return _response(result.get("status", "failed"), result.get("message", ""), result)
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for getting asset list from DB
'''
def get_mgn_performance_uploads(record: PerformanceUploadsRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_mgn_performance_uploads", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))      
