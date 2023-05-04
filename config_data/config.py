from environs import Env

env = Env()
env.read_env()

OPENAI_API_KEY = env("OPENAI_API_KEY")
BOT_TOKEN = env("BOT_TOKEN")
ADMIN_IDS = env("ADMIN_IDS")


FFMPEG_BINARY_WINDOWS = f"services/ffmpeg_windows/ffmpeg.exe"
FFMPEG_BINARY_LINUX = f"services/ffmpeg_linux/ffmpeg"

