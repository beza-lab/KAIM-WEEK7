from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

# Create the FastAPI app
app = FastAPI(debug=True)  # Enable debug mode

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Detection API"}

# Define the API endpoints
@app.post("/detection_data/", response_model=schemas.DetectionData)
def create_detection_data(detection_data: schemas.DetectionDataCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_detection_data(db=db, detection_data=detection_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/detection_data/", response_model=list[schemas.DetectionData])
def read_detection_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        detection_data = crud.get_detection_data(db, skip=skip, limit=limit)
        return detection_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
