from aiogram import Bot
from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import LEXICON

router: Router = Router()


@router.message(F.voice | F.audio)
async def send_echo(message: Message, bot: Bot):
    try:
        file_id = message.voice.file_id if message.voice else message.audio.file_id
        await message.reply(text=f"file info \n {file_id}")
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, "some_file.mp3")
    except BaseException as e:
        await message.reply(text=f"Exception...\n {e}")
