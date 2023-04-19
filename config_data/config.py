from environs import Env

env = Env()
env.read_env()

OPENAI_API_KEY = env("OPENAI_API_KEY")
BOT_TOKEN = env("BOT_TOKEN")
OPENAI_API_KEY_FROM_HRY = env("OPENAI_API_KEY_FROM_HRY")
ADMIN_IDS = env("ADMIN_IDS")

