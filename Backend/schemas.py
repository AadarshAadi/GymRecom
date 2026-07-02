from pydantic import BaseModel
from typing import List
class WR(BaseModel):
    woty: str
    days: int
    age: int
    duration: int
    exp: str
    aequip: List[str]
    injury: str