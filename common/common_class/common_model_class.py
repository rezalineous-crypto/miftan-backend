from typing import Optional
from pydantic import BaseModel, Field

class BaseEntity(BaseModel):
    by_user_id: Optional[int] = Field(..., description="Auto-injected from request.user.id")
    start_record: Optional[int] = None
    page_size: Optional[int] = None