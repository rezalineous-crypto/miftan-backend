import datetime
import uuid
import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings

def _response(status, message, data=None):
    return {
        "status": status,
        "message": message,
        "data": data or []
    }


def inject_user_id(data, user_id):
    """
    Recursively inject 'by_user_id' into all dicts in the data,
    including nested dicts and list of dicts.
    """
    if isinstance(data, dict):
        # Add by_user_id to current dict if not present
        data.setdefault("by_user_id", user_id)
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                inject_user_id(value, user_id)
    elif isinstance(data, list):
        for item in data:
            inject_user_id(item, user_id)
    return data


def build_request_with_user(model_class, request, method='GET'):
    data = request.query_params.dict() if method == 'GET' else request.data
    print(data)
    #payload = {**data, "by_user_id": request.user.id}
    payload = inject_user_id(dict(data), request.user.id)
    print(request)
    return model_class(**payload)



def generate_tokens(user_data: dict):
    now = datetime.now(timezone.utc)

    jti = str(uuid.uuid4())

    access_payload = {
        "user_id": user_data["user_id"],
        "type": "access",
        "exp": now + timedelta(minutes=15),
        "iat": now
    }

    refresh_payload = {
        "user_id": user_data["user_id"],
        "type": "refresh",
        "jti": jti,
        "exp": now + timedelta(days=7),
        "iat": now
    }

    access_token = jwt.encode(access_payload, settings.SECRET_KEY, algorithm="HS256")
    refresh_token = jwt.encode(refresh_payload, settings.SECRET_KEY, algorithm="HS256")

    return access_token, refresh_token, jti, refresh_payload["exp"]