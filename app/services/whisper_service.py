import whisper

model = whisper.load_model("base")  # You can also use "small", "medium", "large"

def transcribe_audio(file_path: str) -> str:
    result = model.transcribe(file_path)
    return result["text"]
