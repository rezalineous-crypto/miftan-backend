from datetime import datetime
from typing import List, Optional

from common.common_class.common_model_class import BaseEntity


class CompaniesRequest(BaseEntity):
    id: int = None
    name: Optional[str] = None
    code: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None


class OwnersRequest(BaseEntity):
    id: int = None
    company_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None 

class PropertiesRequest(BaseEntity):
    id: int = None
    company_id: int = None
    property_code: Optional[str] = None
    property_name: Optional[str] = None
    owner_id: Optional[int] = None
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    remarks: Optional[str] = None  

class PropertyDiagnosisRulesRequest(BaseEntity):
    id: int = None
    rule_code: Optional[str] = None
    priority: int = None
    pace_min: Optional[float] = None
    pace_max: Optional[float] = None
    nights_min: Optional[float] = None
    nights_max: Optional[float] = None
    adr_min: Optional[float] = None
    adr_max: Optional[float] = None
    status: Optional[str] = None
    category: Optional[str] = None
    action_type: Optional[str] = None
    adr_multiplier: Optional[float] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None    

class PropertyMonthlyConfigRequest(BaseEntity):
    id: int = None
    property_id: int = None
    year: int = None
    month: int = None
    market_adr: Optional[float] = None
    market_occupancy: Optional[float] = None
    paf: Optional[float] = None
    pace_threshold: Optional[float] = None
    nights_low_threshold: Optional[float] = None
    nights_high_threshold: Optional[float] = None
    adr_low_threshold: Optional[float] = None
    adr_high_threshold: Optional[float] = None
    early_month_guard_days: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None


class PropertyPerformanceRequest(BaseEntity):
    id: Optional[int] = None
    company_id: Optional[int] = None
    property_id: Optional[int] = None
    date: Optional[datetime] = None
    rooms: Optional[int] = None
    revenue: Optional[float] = None
    source_upload_id: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None

#Report Modal
class PropertyDiagnosisRequest(BaseEntity):
    property_id: Optional[int] = None
    month: Optional[datetime] = None
