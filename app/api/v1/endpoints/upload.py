from fastapi import APIRouter, UploadFile, File
from app.models.upload import UploadResponse
from app.core.csv.parser import CSVParser
from app.utils.exceptions import AppException
from app.config import settings

router = APIRouter()

@router.post("/", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise AppException(status_code=400, message="Only .csv files are allowed")

    contents = await file.read()

    if len(contents) > settings.max_file_size_mb * 1024 * 1024:
        raise AppException(status_code=413, message=f"File exceeds {settings.max_file_size_mb}MB limit")

    result = CSVParser.parse(contents)

    return UploadResponse(filename=file.filename, **result)