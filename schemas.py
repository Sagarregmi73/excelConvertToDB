from pydantic import BaseModel
from typing import Union

class RecordSchema(BaseModel):
    part_number: str
    year: int
    category: str
    model: str
    vehicle_type: str
    color: str
    price: float
    stock: int
