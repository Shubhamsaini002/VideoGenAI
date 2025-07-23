import os
from fastapi import UploadFile
import shutil

UPLOAD_FOLDER = "uploads"

async def save_upload_file(file: UploadFile) -> str:
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_path
