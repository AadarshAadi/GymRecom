from pydantic import BaseModel
from typing import List
class WR(BaseModel):
    workcat: str
    days: int
    age: int
    duration: int
    exper: str
    equipm: List[str]
    injury: str