import subprocess
from config_data.config import FFMPEG_BINARY_WINDOWS, FFMPEG_BINARY_LINUX

FFMPEG_BINARY = FFMPEG_BINARY_LINUX
# FFMPEG_BINARY = FFMPEG_BINARY_WINDOWS


def convert_audio_to_mp3(file_bytes: bytes = None,
                         path_input=None,
                         file_name='default_name',
                         speed=1.4) -> bytes | None:
    bitrate = "33k"

    if path_input or file_name.split(".")[-1] in ['mp4', 'aac', 'mkv', 'avi', 'mov', 'webm', 'mpg']:
        if not path_input:
            path_input = f"temp/{file_name}"
            with open(path_input, "wb") as temp_file:
                temp_file.write(file_bytes)

        command = [FFMPEG_BINARY, "-i", path_input, "-b:a", bitrate, "-filter:a",
                   f"atempo={speed}", "-f", "mp3", "pipe:"]
        output_data = subprocess.run(command, stdout=subprocess.PIPE, check=True)
        return output_data.stdout

    if file_bytes:
        command = [FFMPEG_BINARY, "-i", "pipe:", "-b:a", bitrate,
                   "-filter:a", f"atempo={speed}", "-f", "mp3", "pipe:"]
        output_data = subprocess.run(command, input=file_bytes, stdout=subprocess.PIPE, check=True)
        return output_data.stdout
