from pydantic import BaseModel

class UploadResponse(BaseModel):
    columns: list[str]
    preview: list[dict]
