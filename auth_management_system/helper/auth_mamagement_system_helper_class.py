import datetime
from time import timezone

import jwt
import psycopg2
from django.conf import settings
import json
from auth_management_system.helper.model_class import UserEntityAccessRequest, UsersRequest
from common.common_class.db import call_db_function, get_db_connection
from common.common_class.util import _response, generate_tokens

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for getting asset list from DB
'''
def validate_user_login(record: UsersRequest):
    try:
        with get_db_connection() as conn:
            rows = call_db_function(
                conn,
                "public.validate_user_login",
                [record.json()]
            )

            if not rows:
                return _response("failed", "No response from server")

            result = rows[0]
            data = result.get("data")

            if isinstance(data, str):
                data = json.loads(data)

            if result.get("status") == "success" and data:

                access, refresh, jti, exp = generate_tokens(data)

                # ✅ JSON payload for DB function
                session_payload = {
                    "user_id": data["user_id"],
                    "refresh_token": refresh,
                    "jti": jti,
                    "expires_at": exp.isoformat() if hasattr(exp, "isoformat") else str(exp)
                }

                session_result = call_db_function(
                    conn,
                    "public.fn_insert_auth_user_sessions",
                    [json.dumps(session_payload)]
                )

                session_status = session_result[0].get("status")

                if session_status != "success":
                    return _response("error", session_result[0].get("message"))

                data.update({
                    "access_token": access,
                    "refresh_token": refresh
                })

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))
    

# refresh token api POST /token/refresh
def refresh_access_token(refresh_token: str):
    try:
        # 1. Decode refresh token
        payload = jwt.decode(
            refresh_token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )

        jti = payload["jti"]
        user_id = payload["user_id"]

        # 2. Validate session via DB function
        session_payload = {
            "jti": jti,
            "user_id": user_id
        }

        with get_db_connection() as conn:
            rows = call_db_function(
                conn,
                "public.fn_validate_refresh_session",
                [json.dumps(session_payload)]
            )

        result = rows[0]

        if result.get("status") != "success":
            return _response("failed", result.get("message"))

        # 3. Generate new access token
        access_payload = {
            "user_id": user_id,
            "type": "access",
            "exp": datetime.now(timezone.utc) + datetime.timedelta(minutes=15),
            "iat": datetime.now(timezone.utc)
        }

        access_token = jwt.encode(
            access_payload,
            settings.SECRET_KEY,
            algorithm="HS256"
        )

        return _response("success", "Token refreshed", {
            "access_token": access_token
        })

    except Exception as ex:
        return _response("error", str(ex)) 
    
#POST /logout
def logout_user(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
        jti = payload["jti"]

        with get_db_connection() as conn:
            conn.execute("""
                UPDATE public.user_sessions
                SET is_active = FALSE
                WHERE jti = %s
            """, (jti,))

        return _response("success", "Logged out successfully")

    except Exception as ex:
        return _response("error", str(ex))    
    


def insert_auth_user(record: UsersRequest):
    try:
        with get_db_connection() as conn:
            rows = call_db_function(
                conn,
                "public.fn_insert_auth_user",
                [record.json()]
            )

            if not rows:
                return _response("failed", "No response from server")

            result = rows[0]
            data = result.get("data")

            if isinstance(data, str):
                data = json.loads(data)

            return _response(
                result.get("status"),
                result.get("message"),
                data
            )

    except Exception as ex:
        return _response("error", str(ex))
    


def insert_user_entity_access(record: UserEntityAccessRequest):
    try:
        with get_db_connection() as conn:
            rows = call_db_function(
                conn,
                "public.fn_insert_auth_user_entity_access",
                [record.json()]
            )

            if not rows:
                return _response("failed", "No response from server")

            result = rows[0]
            data = result.get("data")

            if isinstance(data, str):
                data = json.loads(data)

            return _response(
                result.get("status"),
                result.get("message"),
                data
            )

    except Exception as ex:
        return _response("error", str(ex))    
    

def get_auth_user_entity_access(record: UserEntityAccessRequest):
    try:
        with get_db_connection() as conn:
            rows = call_db_function(
                conn,
                "public.fn_get_auth_user_entity_access",
                [record.json()]
            )

            if not rows:
                return _response("failed", "No response from server")

            result = rows[0]
            data = result.get("data")

            if isinstance(data, str):
                data = json.loads(data)

            return _response(
                result.get("status"),
                result.get("message"),
                data
            )

    except Exception as ex:
        return _response("error", str(ex))  
