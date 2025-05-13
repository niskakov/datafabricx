from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO

from .parsers import parse_csv, parse_excel, parse_pdf
from .transformer import normalize_column_names
from .models import UploadResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    ext = file.filename.split(".")[-1].lower()

    if ext == "csv":
        df = parse_csv(BytesIO(contents))
    elif ext in ["xls", "xlsx"]:
        df = parse_excel(BytesIO(contents))
    elif ext == "pdf":
        df = parse_pdf(BytesIO(contents))
    else:
        return {"columns": [], "preview": []}

    df.columns = normalize_column_names(df.columns.tolist())
    preview = df.fillna("").head(10).to_dict(orient="records")
    return {"columns": df.columns.tolist(), "preview": preview}

@app.get("/")
def root():
    return {"message": "DataFabricX API is running!"}
