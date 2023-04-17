import subprocess
from datetime import datetime

data_time = datetime.now().strftime("%m-%d_%H-%M-%S")

input_file = f"../tests/samples/input.ogg"

output_file = f"../tests/samples/output_audio/{data_time}.mp3"

FFMPEG_BINARY = f"../ffmpeg.exe"


command = [FFMPEG_BINARY, "-i", input_file, output_file]

subprocess.run(command, check=True)

