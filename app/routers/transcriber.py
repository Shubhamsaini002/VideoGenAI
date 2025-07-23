from fastapi import APIRouter, UploadFile, File
from app.services.whisper_service import transcribe_audio
from app.utils.file_utils import save_upload_file

router = APIRouter()

@router.post("/transcribe-audio")
async def transcribe(file: UploadFile = File(...)):
    file_path = await save_upload_file(file)
    transcript = transcribe_audio(file_path)
    return {"transcription": transcript}
