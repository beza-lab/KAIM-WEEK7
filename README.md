Task 1 - Data scraping and collection pipeline
Telegram Scraping: Utilize the Telegram API or write custom scripts to extract data from public Telegram channels relevant to Ethiopian medical businesses. Use the following channels
https://t.me/DoctorsET
Chemed Telegram Channel
https://t.me/lobelia4cosmetics
https://t.me/yetenaweg
https://t.me/EAHCI
And many more from https://et.tgstat.com/medicine

Image and Scraping: Collect images from the following telegram channels for object detection:
Chemed Telegram Channel
https://t.me/lobelia4cosmetics
Steps:
Use Python packages like:
For telegram: telethon
Developing Telegram data extraction scripts or simply exporting content using the Telegram application.
 Storing Raw Data:
Initial Storage: Store the raw scraped data in a temporary storage location, such as a local database or files, before processing it further.
Monitoring and Logging:
Logging: Implement logging to track the scraping process, capture errors, and monitor progress.

Task 2 -  Data Cleaning and Transformation
Data Cleaning:
Removing Duplicates
Handling Missing Values
Standardizing Formats
Data Validation
Storing Cleaned Data
Database Storage
DBT for Data Transformation:
Setting Up DBT: Install DBT (Data Build Tool) and set up a DBT project.
pip install dbt
dbt init my_project
Defining Models
Create DBT models for data transformation. DBT models are SQL files that define transformations on your data.
Run the DBT models to perform the transformations and load the data into your data warehouse.
dbt run
Testing and Documentation: Use DBT’s testing and documentation features to ensure data quality and provide context for the transformations.
dbt test
dbt docs generate
dbt docs serve

Monitoring and Logging:
Logging: Implement logging to track the scraping process, capture errors, and monitor progress.

Task 3 - Object Detection Using YOLO

Setting Up the Environment:
Ensure you have the necessary dependencies installed, including YOLO and its required libraries (e.g., OpenCV, TensorFlow, or PyTorch depending on the YOLO implementation).
pip install opencv-python
pip install torch torchvision  # for PyTorch-based YOLO
pip install tensorflow  # for TensorFlow-based YOLO

Downloading the YOLO Model
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
Preparing the Data
 Collect images from the Chemed Telegram Channel, https://t.me/lobelia4cosmetics
Use the pre-trained YOLO model to detect objects in the images.
Processing the Detection Results
Extract relevant data from the detection results, such as bounding box coordinates, confidence scores, and class labels.
Storing detection data to a database table.
Monitoring and Logging:
Logging: Implement logging to track the scraping process, capture errors, and monitor progress.

Task 4 - Expose the collected data using Fast API 
Setting Up the Environment:
Install FastAPI and Uvicorn
pip install fastapi uvicorn
Create a FastAPI Application
Set up a basic project structure for your FastAPI application.
my_project/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py
Database Configuration
In the database.py configure the database connection using SQLAlchemy.
Creating Data Models
In the models.py define SQLAlchemy models for the database tables.
Creating Pydantic Schemas
In the schemas.py define Pydantic schemas for data validation and serialization.
CRUD Operations
In the crud.py implement CRUD (Create, Read, Update, Delete) operations for the database.
Creating API Endpoints
In the main.py define the API endpoints using FastAPI.
