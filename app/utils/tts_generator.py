from gtts import gTTS
import os

def generate_test_mp3(text: str, filename: str = "test_audio.mp3", save_dir: str = "uploads") -> str:
    os.makedirs(save_dir, exist_ok=True)
    output_path = os.path.join(save_dir, filename)
    tts = gTTS(text)
    tts.save(output_path)
    return output_path
