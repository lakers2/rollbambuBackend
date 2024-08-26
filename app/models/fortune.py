from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Fortune(Base):
    __tablename__ = "fortunes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    interpretation = Column(String)