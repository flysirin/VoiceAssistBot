import io
import subprocess
from datetime import datetime
from typing import BinaryIO

FFMPEG_BINARY = f"services/ffmpeg.exe"


def convert_audio_to_mp3(file_bytes: BinaryIO = None, path_input=None, file_name=None, path_output=None):
    data_time = datetime.now().strftime("%m-%d_%H-%M-%S")
    file_name = (file_name or data_time).split(".")[0]
    speed = 1
    bitrate = "64k"
    if path_input:
        output_default = f"tests/output_files/{file_name}.mp3"
        path_output = path_output or output_default
        command = [FFMPEG_BINARY, "-i", path_input, "-b:a", bitrate, "-filter:a", f"atempo={speed}", path_output]
        subprocess.run(command, check=True)
        return path_output
    if file_bytes:
        command = [FFMPEG_BINARY, "-f", "aac", "-i", "pipe:", "-b:a", bitrate, "-filter:a", f"atempo={speed}", "-f", "mp3", "pipe:"]
        output_data = subprocess.run(command, stdin=file_bytes, stdout=subprocess.PIPE, check=True)

        return output_data.stdout
