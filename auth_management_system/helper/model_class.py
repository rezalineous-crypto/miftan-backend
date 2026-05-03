from datetime import datetime
from typing import List, Optional

from common.common_class.common_model_class import BaseEntity


class RolesRequest(BaseEntity):
    id: int = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None


class UserCompaniesRequest(BaseEntity):
    user_id: int = None
    company_id: int = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None    

class UsersRequest(BaseEntity):
    id: Optional[int] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    full_name: Optional[str] = None
    role_id: Optional[int] = None
    is_super_admin: Optional[bool] = None
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    remarks: Optional[str] = None    

class UserEntityAccessRequest(BaseEntity):
    id: Optional[int] = None
    user_id: Optional[int] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    is_active: Optional[bool] = None    