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
