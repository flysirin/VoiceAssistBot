import subprocess
from logging import debug, info
import json

from services import convert_audio
from config_data.config import OPENAI_API_KEY_FROM_HRY

TRANSCRIPTIONS_URL = 'https://api.openai.com/v1/audio/transcriptions'
CHAT_URL = 'https://api.openai.com/v1/chat/completions'


# OPENAI_API_KEY = OPENAI_API_KEY_FROM_HRY


def transcribe_audio_to_text(file_bytes: bytes = None,
                             file_name: str = 'default_name.mp3',
                             path: str = None) -> str:
    debug('start')

    result_text = ''
    path_save_txt = f"temp/{file_name.split('.')[0]}.txt"
    model = "whisper-1"

    curl_command = ['curl.exe', '--request', 'POST',
                    '--url', f'{TRANSCRIPTIONS_URL}',
                    '--header', f'Authorization: Bearer {OPENAI_API_KEY_FROM_HRY}',
                    '--header', 'Content-Type: multipart/form-data',
                    '--form', f'file=@-;filename=file_name.mp3',
                    '--form', f'model={model}']

    # '--form', 'response_format=text']

    def curl_post_request(bytes_f):
        res = subprocess.run(curl_command,
                             input=bytes_f,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=True)
        if res.returncode == 0:
            return json.loads(res.stdout)

    dict_res = curl_post_request(file_bytes)
    if dict_res and "text" in dict_res:
        result_text = dict_res["text"]

    elif "error" in dict_res and "Invalid file format" in dict_res["error"]["message"]:
        try:
            file_bytes = convert_audio.convert_audio_to_mp3(file_bytes=file_bytes, speed=1)
            dict_res = curl_post_request(file_bytes)
            result_text = dict_res.get("text", "Ups..")
        except BaseException as e:
            print("Something wrong", e)

    if result_text:
        with open(path_save_txt, "w", encoding="utf-8") as f:
            f.write(result_text)
            return path_save_txt

    debug('finish')

#
# file_path = f"../tests/output_files/48655.mp3"
# with open(file_path, "rb") as file:
#     print(transcribe_audio_to_text(file.read()))
