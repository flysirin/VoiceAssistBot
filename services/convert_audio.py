import io
import subprocess
from datetime import datetime
from typing import BinaryIO
from pathlib import Path
from config_data.config import FFMPEG_BINARY


def convert_audio_to_mp3(file_bytes: BinaryIO = None,
                         path_input=None,
                         file_name=None) -> bytes:

    data_time = datetime.now().strftime("%m-%d_%H-%M-%S")
    file_name = (file_name or data_time)
    speed = 1.4
    bitrate = "33k"

    if path_input or file_name.split(".")[-1] == "aac":
        if not path_input:
            path_input = f"temp/{file_name}"
            with open(path_input, "wb") as temp_file:
                temp_file.write(file_bytes.read())

        command = [FFMPEG_BINARY, "-i", path_input, "-b:a", bitrate, "-filter:a",
                   f"atempo={speed}", "-f", "mp3", "pipe:"]
        output_data = subprocess.run(command, stdout=subprocess.PIPE, check=True)
        return output_data.stdout

    if file_bytes:
        command = [FFMPEG_BINARY, "-i", "pipe:", "-b:a", bitrate,
                   "-filter:a", f"atempo={speed}", "-f", "mp3", "pipe:"]
        file_bytes = file_bytes.read()  # Read BinaryIO obj
        output_data = subprocess.run(command, input=file_bytes, stdout=subprocess.PIPE, check=True)
        return output_data.stdout


def delete_temp_files(path: str = "temp"):
    folder = Path(path)
    for file in folder.glob("*"):
        if file.is_file() and file.name != ".gitignore":
            try:
                file.unlink()
            except BaseException as e:
                print(f"File '{file}', can not delete. \n{e}")
