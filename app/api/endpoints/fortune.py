from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
import random
from app.models.fortune import Fortune
from pydantic import BaseModel
import logging

router = APIRouter()

logger = logging.getLogger(__name__)

class FortuneSchema(BaseModel):
    name: str
    interpretation: str

    class Config:
        orm_mode = True

@router.get("/fortune")
def get_fortune(db: Session = Depends(get_db)):
    fortunes = db.query(Fortune).all()
    if not fortunes:
        logger.error("没有可用的运势")
        return {"error": "没有可用的运势"}
    
    random_fortune = random.choice(fortunes)
    logger.info(f"选中的运势: {random_fortune.name}, 解析: {random_fortune.interpretation}")
    return {
        "fortune": random_fortune.name,
        "interpretation": random_fortune.interpretation
    }

@router.post("/fortune", response_model=FortuneSchema)
async def create_fortune(fortune: FortuneSchema, db: Session = Depends(get_db)):
    db_fortune = Fortune(**fortune.dict())
    db.add(db_fortune)
    db.commit()
    db.refresh(db_fortune)
    return db_fortune