import os
import uuid
from datetime import datetime
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import database, models

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database.Base.metadata.create_all(bind=database.engine)
UPLOAD_DIR = "./uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Upload file API
@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    system_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, system_name)

    # Save file locally
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    db = database.SessionLocal()
    file_record = models.File(
        original_filename=file.filename,
        system_filename=system_name,
        file_size_bytes=os.path.getsize(file_path),
    )
    db.add(file_record)
    db.commit()
    db.refresh(file_record)
    db.close()

    return {"message": "File uploaded successfully!"}

# Fetch all uploaded files
@app.get("/files")
def get_files():
    db = database.SessionLocal()
    files = db.query(models.File).all()
    db.close()

    # Convert datetime to readable string
    return [
        {
            "original_filename": f.original_filename,
            "file_size_bytes": f.file_size_bytes,
            "uploaded_at": f.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for f in files
    ]
