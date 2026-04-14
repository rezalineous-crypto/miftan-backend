from datetime import datetime
from typing import List, Optional

from common.common_class.common_model_class import BaseEntity


class PerformanceUploadDetailsRequest(BaseEntity):
    id: int = None
    upload_id: Optional[int] = None
    stay_date: Optional[datetime] = None
    hotel_name: Optional[str] = None
    rooms: Optional[int] = None
    arrivals: Optional[int] = None
    departures: Optional[int] = None
    stay_over: Optional[int] = None
    total_income: Optional[float] = None
    average_room_rate: Optional[float] = None
    bed_nights: Optional[int] = None
    average_guest_rate: Optional[float] = None
    occupancy_percentage: Optional[float] = None
    guest_per_room: Optional[float] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None


class PerformanceUploadsRequest(BaseEntity):
    id: int = None
    company_id: int = None
    property_id: int = None
    file_name: Optional[str] = None
    upload_month: Optional[int] = None
    upload_year: Optional[int] = None
    upload_date: Optional[datetime] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None
