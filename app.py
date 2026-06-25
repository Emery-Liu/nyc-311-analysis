from fastapi import FastAPI, UploadFile, File, HTTPException

import pandas as pd
import uvicorn
from fastapi.staticfiles import StaticFiles

from src.mapping_config import FIELD_MAPPING
from src.cleaning import add_resolution_col
from src.analysis import resolution_summary
from src.visualization import plot_images
from src.model import SummaryResponse
from src.database import get_filename_by_id, insert_upload, init_database

app = FastAPI()
init_database()
app.mount("/static", StaticFiles(directory="figures"), name="static") #AI gen


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")
    try:
        # save csv to uploads
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        # import to SQLite
        file_id = insert_upload(file.filename)
        # return file_id
        return {"message": "File uploaded and processed successfully.",
                "file_id": file_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")


@app.get("/summary/{file_id}", response_model=SummaryResponse)
def get_summary(file_id: int):
    row = get_filename_by_id(file_id)
    if row is None:
        raise HTTPException(
            status_code = 404,
            detail = "File not found"
        )
    filename  = row[0]
    
    df = pd.read_csv(f"uploads/{filename}")

    df.rename(
            columns=FIELD_MAPPING,
            inplace=True
        )
    df = add_resolution_col(df)

    return resolution_summary(df)


@app.post("/generate-plots/{file_id}")
def generate_plots(file_id: int):
    try:
        row = get_filename_by_id(file_id)

        if row is None:
            raise HTTPException(
                status_code=404,
                detail="File not found."
            )
        filename = row[0]
        df = pd.read_csv(f"uploads/{filename}")
        df.rename(columns=FIELD_MAPPING,inplace=True)
        df = add_resolution_col(df)
        plot_images(df)
        
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
                f"{base_url}/request_heatmap.html"
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
