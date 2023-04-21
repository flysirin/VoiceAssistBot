import io
import openai
from config_data import config
from datetime import datetime

openai.api_key = config.OPENAI_API_KEY_FROM_HRY


def transcribe_audio_to_text(file_bytes: bytes = None, file_name: str = None, path: str = None) -> str:
    """Decode audio and save to txt file"""
    if path and not file_bytes:
        with open(path, "rb") as audio_file_binary:
            file_bytes = audio_file_binary.read()
    transcript = openai.Audio.transcribe_raw("whisper-1", file_bytes, "some_file.mp3")

    path_save_txt = f"temp/{file_name.split('.')[0]}.txt"
    with open(path_save_txt, 'w', encoding="utf-8") as f:
        f.write(transcript["text"])

    return path_save_txt


def text_request_to_open_ai(text: str = "Hello!") -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Краткое содержание этого текста {text}"}
        ]
    )
    return completion.choices[0].message["content"]

# text_file = f"../tests/load_files/19537079.txt"
# with open(text_file, "r", encoding="utf-8") as f:
#     print(text_request_to_open_ai(f.read()))

