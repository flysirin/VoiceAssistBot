# import subprocess
# FFMPEG_BINARY = f"../services/ffmpeg.exe"
#
# speed = 1
# bitrate = "64k"
# file_path = "../tests/load_files/step_1.aac"
# with open(file_path, "rb") as bytes_file, open("file.mp3", "wb") as save_file:
#     command = [FFMPEG_BINARY, "-i", "pipe:", "-b:a", bitrate, "-filter:a", f"atempo={speed}", "-f", "mp3", "pipe:"]
#     output_data = subprocess.run(command, stdin=bytes_file, stdout=subprocess.PIPE, check=True)
#     save_file.write(output_data.stdout)
#

# ---------------------------------------------------------------------------------------------------------------------


import subprocess

# FFMPEG_BINARY = f"../services/ffmpeg.exe"
#
# speed = 1
# bitrate = "64k"
# file_path = "../tests/load_files/step_1.aac"
# with open(file_path, "rb") as bytes_file, open("file.mp3", "wb") as save_file:
#     command = [FFMPEG_BINARY, "-i", "pipe:", "-b:a", bitrate, "-filter:a", f"atempo={speed}", "-f", "mp3", "pipe:"]
#     out = subprocess.run(command, input=bytes_file.read(), stdout=subprocess.PIPE)
#     save_file.write(out.stdout)


# ---------------------------------------------------------------------------------------------------------------------
#
# import subprocess
#
# FFMPEG_BINARY = "../services/ffmpeg.exe"
#
# speed = 1
# bitrate = "64k"
# file_path = "../tests/load_files/step_1.aac"
# with open(file_path, "rb") as bytes_file, open("file.mp3", "wb") as save_file:
#     command = [FFMPEG_BINARY, "-i", "pipe:", "-b:a", bitrate, "-filter:a", f"atempo={speed}", "-f", "mp3", "pipe:"]
#     proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#     out, _ = proc.communicate(input=bytes_file.read())
#     save_file.write(out)

# ---------------------------------------------------------------------------------------------------------------------
