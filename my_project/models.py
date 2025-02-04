from sqlalchemy import Column, Integer, String, Float
from database import Base  # Use absolute import

class DetectionData(Base):
    __tablename__ = "detection_data"

    id = Column(Integer, primary_key=True, index=True)
    x_min = Column(Float, index=True)
    y_min = Column(Float, index=True)
    x_max = Column(Float, index=True)
    y_max = Column(Float, index=True)
    confidence = Column(Float, index=True)
    class_id = Column(Integer, index=True)
    name = Column(String, index=True)
