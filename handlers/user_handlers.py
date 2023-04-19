# import io

from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON
from services import convert_audio

# Initialise router by module level
router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])


# First func version for download sound
# @router.message(F.voice | F.audio)
# async def process_download_audio(message: Message, bot: Bot):
#     try:
#         file_id = message.voice.file_id if message.voice else message.audio.file_id
#         file_name = f"{message.voice.file_size}.ogg" if message.voice else message.audio.file_name
#         file = await bot.get_file(file_id)
#         await message.reply(text=f"file info \n {file_name}")
#         file_path = file.file_path
#         await bot.download_file(file_path, f"tests/load_file/{file_name}")
#     except BaseException as e:
#         await message.reply(text=f"Exception...\n {e}")


# Second version func for download sound with read binary
@router.message(F.voice | F.audio)
async def process_audio_to_text(message: Message, bot: Bot):
    try:
        file = message.voice if message.voice else message.audio
        file_name = f"{message.voice.file_size}.ogg" if message.voice else message.audio.file_name

        sound_binary_io = await bot.download(file)
        sound_bytes = sound_binary_io.read()
        with open(f"tests/load_files/{file_name}", "wb") as f:
            f.write(sound_bytes)
        await message.reply(text=f"Success download: \n{file_name}")

        path_for_convert = f"tests/load_files/{file_name}"
        path_output = convert_audio.convert_audio_to_mp3(file_name=file_name, path_input=path_for_convert)

        await message.reply(text=f"Success convert to mp3: \n{path_output}")
    except BaseException as e:
        await message.reply(text=f"Exception: \n{e}")

