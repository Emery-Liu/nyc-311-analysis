# How to use
1. Download a NYC 311 CSV file.
2. Place it in data/raw/.
3. Rename it to: nyc_311_2025_sample.csv
4. Run: python src/main.py



# NYC 311 Service Requests Analysis

This project explores NYC 311 service request data using Python, Pandas, NumPy, and Matplotlib.

The goal is to understand:

- Which complaint types are most common
- Which NYC boroughs receive the most complaints
- How long different complaints take to resolve
- Which agencies handle requests most efficiently
- Where complaints are geographically concentrated

The analysis is based on a sample of 50,000 NYC 311 service requests collected from NYC Open Data.

## Project Structure

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

figures/
reports/

## Data Source

NYC Open Data: 311 Service Requests from 2020 to Present

Dataset page:
https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9

This project uses a filtered sample dataset:

'data/raw/nyc_311_2025_sample.csv'

## Analysis Performed

**Data Cleaning**

- Missing value inspection
- Datetime conversion
- Resolution time calculation
- Geographic coordinate cleaning

**Complaint Analysis**

- Complaint volume by agency
- Complaint volume by borough
- Top complaint categories

**Resolution Time Analysis**

- Mean resolution time
- Median resolution time
- 95th percentile analysis
- Resolution time by complaint type
- Resolution time by agency

**Spatial Analysis**

- Complaint density heatmap using latitude and longitude