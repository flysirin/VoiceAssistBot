import subprocess

FFMPEG_BINARY = r"C:\\python_projects\\Education\\VoiceAssistBot\\ffmpeg.exe"
input_file = r"C:\\python_projects\\Education\\VoiceAssistBot\\tests\\samples\\input.wav"
# output_file = r"../tests/samples/output.ogg"

# command = [FFMPEG_BINARY, '-i', input_file, output_file]

command = [FFMPEG_BINARY, '-i', input_file, '-af', 'silencedetect=noise=-50dB:d=0.5', '-f', 'null', '-', '2>', 'output.txt']

with open('output.txt', 'w') as f:
    subprocess.run(command, check=True, stderr=f)
