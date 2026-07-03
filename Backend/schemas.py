from pydantic import BaseModel
from typing import List
class WR(BaseModel):
    workout_type: str
    days: int
    age: int
    duration: int
    experience_level: str
    available_equipment: List[str]
    injury: str