from pydantic import BaseModel

class UploadResponse(BaseModel):
    filename: str
    rows: int
    columns: list[str]
    dtypes: dict[str, str]
    preview: list[dict]