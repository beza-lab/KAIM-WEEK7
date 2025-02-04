from pydantic import BaseModel

class DetectionDataBase(BaseModel):
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    confidence: float
    class_: int  # Ensuring class_ matches the model attribute
    name: str

class DetectionDataCreate(DetectionDataBase):
    pass

class DetectionData(DetectionDataBase):
    id: int

    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'
