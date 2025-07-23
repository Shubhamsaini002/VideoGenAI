from fastapi import APIRouter, UploadFile, File, Form
from app.services.whisper_service import transcribe_audio
from app.utils.file_utils import save_upload_file
from app.utils.tts_generator import generate_test_mp3
router = APIRouter()

@router.post("/generate-mp3-to-text")
async def transcribe(file: UploadFile = File(...)):
    file_path = await save_upload_file(file)
    transcript = transcribe_audio(file_path)
    return {"transcription": transcript}
@router.post("/generate-text-to-mp3")
async def generate_mp3(text: str = Form(...)):
    file_path = generate_test_mp3(text)
    return {"file_path": file_path}
