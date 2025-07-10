from fastapi import APIRouter, UploadFile, File
from src.models.delay_forecast import forecast_delay
import os

router = APIRouter()

@router.post("/forecast_delay", tags=["TimeSeries"])
def forecast_delay_endpoint(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    result = forecast_delay(file_path)
    return result