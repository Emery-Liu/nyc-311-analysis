# How to use
1. Ensure you have the required dependencies installed.
2. Check your current directory by pwd, cd to the folder root directory, then run
    uvicorn app:app --reload
3. Access http://127.0.0.1:8000/docs to interact with SwaggerUI

# NYC 311 Service Requests Analysis

This project explores NYC 311 service request data using Python, Pandas, NumPy, and Matplotlib.

The goal is to understand:

- Which complaint types are most common
- Which NYC boroughs receive the most complaints
- How long different complaints take to resolve
- Which agencies handle requests most efficiently
- Where complaints are geographically concentrated

The analysis is based on a sample of 50,000 NYC 311 service requests collected from NYC Open Data.

# Project Structure
```
data/
├── raw/          # Original NYC Open Data files
├── processed/    # Cleaned datasets

notebooks/
├── 01_data_loading_cleaning.ipynb
├── 02_complaint_analysis.ipynb
├── 03_resolution_time_analysis.ipynb
├── 04_spatial_analysis.ipynb

src/
├── analysis.py
├── cleaning.py
├── visualization.py
├── model.py

app.py

figures/
```
# Data Source

NYC Open Data: 311 Service Requests from 2020 to Present

Dataset page:
https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9

This project uses a filtered sample dataset:

'data/raw/nyc_311_2025_sample.csv'
##=================================================================================================
# What I Learned
- **Web API Development**: Learned how to build RESTful APIs using **FastAPI** and serve them locally with **Uvicorn**.
- **Data Validation & Schema**: Learned to use **Pydantic's `BaseModel`** to define strict response models, enabling automatic data validation and Swagger UI documentation generation.
- **File Uploads**: Learned how to handle client file uploads using FastAPI's `UploadFile` and process in-memory file streams directly with Pandas.

# What I Practiced
- **API Endpoint Design**: Practiced designing logical API workflows, such as uploading data first, fetching JSON summaries, and triggering background plot generation.
- **Error Handling**: Practiced implementing robust exception handling in API routes using `HTTPException` to provide clear error messages to the client.
- **Data Visualization**: Practiced creating various types of charts (horizontal bars, pie charts, histograms, 2D heatmaps) using Matplotlib and saving them dynamically to a local directory.
