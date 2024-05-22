import io
import requests

from logging import debug, info
import json

from config_data.config import OPENAI_API_KEY

OPENAI_TRANSCRIPTIONS_URL = 'https://api.openai.com/v1/audio/transcriptions'
OPENAI_CHAT_URL = 'https://api.openai.com/v1/chat/completions'


def transcribe_audio_to_text(file_bytes: bytes = None,
                             file_name: str = 'default_name',
                             path: str = None) -> str:
    debug('start')
    # headers = {'Authorization': f'Bearer {OPENAI_API_KEY_FROM_HRY}', }

