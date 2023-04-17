import openai
from config_data import config
from datetime import datetime

openai.api_key = config.OPENAI_API_KEY_FROM_HRY
def start_audio_decode():
    """Decode audio and save to txt file"""
    audio_file = open("tests/samples/output_audio.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    formatted_date = datetime.now().strftime("%y-%m-%d_%H-%M")
    with open(f"tests/{formatted_date}.txt", 'w', encoding="utf-8") as f:
        f.write(transcript["text"])



