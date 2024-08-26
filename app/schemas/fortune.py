from pydantic import BaseModel
from typing import Optional

class FortuneBase(BaseModel):
    name: str
    interpretation: str

class FortuneCreate(FortuneBase):
    pass

class Fortune(FortuneBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True