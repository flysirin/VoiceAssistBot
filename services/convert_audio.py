import subprocess
from datetime import datetime

FFMPEG_BINARY = f"services/ffmpeg.exe"


def convert_audio_to_mp3(file_bytes: bytes = None, file_name=None, path_input=None, path_output=None):
    data_time = datetime.now().strftime("%m-%d_%H-%M-%S")
    file_name = (file_name or data_time).split(".")[0]
    if path_input:
        output_default = f"tests/output_files/{file_name}.mp3"
        path_output = path_output or output_default
        speed = 1.5
        command = [FFMPEG_BINARY, "-i", path_input, "-b:a", "33k", "-filter:a", f"atempo={speed}", path_output]
        subprocess.run(command, check=True)
    return path_output

