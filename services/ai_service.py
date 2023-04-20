
import openai
from config_data import config
from datetime import datetime

openai.api_key = config.OPENAI_API_KEY_FROM_HRY


def transcribe_audio_to_text(path: str = None, file_name: str = None):
    """Decode audio and save to txt file"""
    if path is None:
        return "None"
    with open(path, "rb") as audio_file_binary:
        transcript = openai.Audio.transcribe("whisper-1", audio_file_binary)
    path_save_txt = f"tests/output_files/{file_name.split('.')[0]}.txt"
    with open(path_save_txt, 'w', encoding="utf-8") as f:
        f.write(transcript["text"])

    return path_save_txt


def text_request_to_open_ai(text: str = "Hello!"):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Краткое содержание этого текста {text}"}
        ]
    )
    return completion.choices[0].message["content"]


# text_file = f"../tests/output_files/1456519.txt"
# with open(text_file, "r", encoding="utf-8") as f:
#     print(text_request_to_open_ai(f.read()))
