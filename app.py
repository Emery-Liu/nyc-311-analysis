from fastapi import FastAPI, UploadFile, File, HTTPException

import pandas as pd
import uvicorn
import os # by AI
from fastapi.staticfiles import StaticFiles

from src.cleaning import add_resolution_col
from src.analysis import (resolution_summary, 
                          top10_complaints, 
                          borough_counts, 
                          agency_resolution_time,
                          complaint_resolution_time,
                          top_complaints_by_borough,
                          agency_complaint_counts)
from src.visualization import (plot_top_complaints, 
                               plot_borough_distribution, 
                               plot_agency_resolution,
                               plot_resolution_histogram,
                               plot_agency_complaint_counts,
                               plot_top_complaints_by_borough,
                               plot_heatmap)
from src.model import SummaryResponse


app = FastAPI()

os.makedirs("figures", exist_ok=True) # by AI
app.mount("/static", StaticFiles(directory="figures"), name="static") #by AI

current_df = None


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    global current_df
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")
    try:
        current_df = pd.read_csv(file.file)
        current_df = add_resolution_col(current_df)
        return {"message": "File uploaded and processed successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")


@app.get("/summary", response_model=SummaryResponse)
def get_summary():
    if current_df is None:
        raise HTTPException(status_code=400, detail="No data uploaded. Please upload a CSV first.")
    return resolution_summary(current_df)


@app.post("/generate-plots")
def generate_plots():
    if current_df is None:
        raise HTTPException(status_code=400, detail="No data uploaded. Please upload a CSV first.")
    try:
        plot_top_complaints(top10_complaints(current_df))
        plot_borough_distribution(borough_counts(current_df))
        plot_agency_resolution(agency_resolution_time(current_df))
        plot_resolution_histogram(complaint_resolution_time(current_df))
        plot_agency_complaint_counts(agency_complaint_counts(current_df))
        plot_top_complaints_by_borough(top_complaints_by_borough(current_df))
        plot_heatmap(current_df)
        
        base_url = "https://nyc-311-analysis.onrender.com/static"

        return {
            "message": "Plots generated and saved successfully.",
            "saved_files": [
                f"{base_url}/top_complaints.png",
                f"{base_url}/borough_distribution.png",
                f"{base_url}/avg_agency_resolution_time.png",
                f"{base_url}/agency_resolution_time.png",
                f"{base_url}/agency_complaint_counts.png",     
                f"{base_url}/top_complaints_by_borough.png",
                f"{base_url}/request_heatmap.png"
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating plots: {str(e)}")
    
if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000
    )