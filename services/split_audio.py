import subprocess
from config_data.config import FFMPEG_BINARY_WINDOWS, FFMPEG_BINARY_LINUX


# FFMPEG_BINARY = FFMPEG_BINARY_WINDOWS
FFMPEG_BINARY = FFMPEG_BINARY_LINUX

input_file = f"../tests/load_files/s8aw5ohnix1r1o7jq8.m4a"

command = [FFMPEG_BINARY, '-i', input_file, '-af', 'silencedetect=noise=-50dB:d=0.5', '-f', 'null', '-', '2>', 'output.txt']

with open('output.txt', 'w') as f:
    subprocess.run(command, check=True, stderr=f)


