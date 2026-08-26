from pydantic import BaseModel
from datetime import datetime

class SensorOut(BaseModel):
    id: int
    name: str
    type: str
    location_id: int
    unit: str
    is_active: bool

class ReadingCreate(BaseModel):
    sensor_id: int
    value: float

class ReadingOut(BaseModel):
    id: int
    sensor_id: int
    value: float
    timestamp: datetime

    class Config:
        from_attributes = True