from sqlalchemy import Column, Integer, String, Float
from database import Base

class DetectionData(Base):
    __tablename__ = "detection_data"

    id = Column(Integer, primary_key=True, index=True)
    x_min = Column(Float, index=True)
    y_min = Column(Float, index=True)
    x_max = Column(Float, index=True)
    y_max = Column(Float, index=True)
    confidence = Column(Float, index=True)
    class_ = Column(Integer, index=True, name="class")  # Ensuring class_ is mapped correctly to 'class'
    name = Column(String, index=True)
