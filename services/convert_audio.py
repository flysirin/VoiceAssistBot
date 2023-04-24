import io
import subprocess
from config_data.config import FFMPEG_BINARY


def convert_audio_to_mp3(file_bytes_io: io.BytesIO = None,
                         path_input=None,
                         file_name='default_name') -> bytes | None:
    speed = 1.4
    bitrate = "64k"

    if path_input or file_name.split(".")[-1] == "aac":
        if not path_input:
            path_input = f"temp/{file_name}"
            with open(path_input, "wb") as temp_file:
                temp_file.write(file_bytes_io.read())

        command = [FFMPEG_BINARY, "-i", path_input, "-b:a", bitrate, "-filter:a",
                   f"atempo={speed}", "-f", "mp3", "pipe:"]
        output_data = subprocess.run(command, stdout=subprocess.PIPE, check=True)
        return output_data.stdout

    if file_bytes_io:
        command = [FFMPEG_BINARY, "-i", "pipe:", "-b:a", bitrate,
                   "-filter:a", f"atempo={speed}", "-f", "mp3", "pipe:"]
        file_bytes = file_bytes_io.read()  # Read BytesIO obj
        output_data = subprocess.run(command, input=file_bytes, stdout=subprocess.PIPE, check=True)
        return output_data.stdout



