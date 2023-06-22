import subprocess

from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON
from services import convert_audio, other_services, ai_service_curl   #, ai_service
from aiogram.types.input_file import FSInputFile

from keyboards import keyboards

from random import choice
import logging

logging.basicConfig(level=logging.WARNING)
logger_user_hand = logging.getLogger(__name__)

# Initialise router by module level
router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])


@router.message(F.voice | F.audio | F.document | F.video)
async def process_audio_to_text(message: Message, bot: Bot):
    try:

        file = message.voice or message.audio or message.document or message.video

        if message.voice:
            file_name = f"{message.voice.file_unique_id}.ogg"
        elif message.audio:
            file_name = message.audio.file_name
        elif message.document and message.document.mime_type.split('/')[0] == 'audio':
            file_name = message.document.file_name
        elif message.video \
                and message.video.mime_type.split('/')[1] in ['mp4', 'mkv', 'avi', 'mov', 'webm', 'mpg']:
            file_name = "video." + message.video.mime_type.split('/')[-1]
        else:
            return await message.reply(
                text=f"This is not a support file format")

        if file.file_size > 20.8e6:
            return await message.reply(
                text=f"File is too big. \nPlease use files less then 20Mb")

        sound_bytes_io = await bot.download(file)
        sound_bytes = sound_bytes_io.read()
        answer_message = await message.reply(
            text=f"File downloaded successfully: \n{file_name}\n Text decoding in progress",
            disable_notification=True)

        logger_user_hand.warning(f"File downloaded successfully.\nFile name: {file_name}")

        sound_bytes = convert_audio.convert_audio_to_mp3(file_bytes=sound_bytes, file_name=file_name)

        text_path = ai_service_curl.transcribe_audio_to_text(sound_bytes, file_name)
        send_doc = FSInputFile(text_path)

        await bot.delete_message(message.chat.id, answer_message.message_id)
        await message.answer_document(send_doc,
                                      reply_markup=keyboards.create_inline_kb())

        other_services.delete_temp_files()

    except subprocess.SubprocessError as ex:
        logger_user_hand.warning(f"{ex}")
        await message.reply(text=f"{choice(LEXICON['wrong_decode'])}")

    except BaseException as e:
        await message.reply(text=f"{choice(LEXICON['another_wrong'])} \n{e}")


@router.callback_query(Text(text=['read_text_button_pressed']))
async def process_read_text_press(callback: CallbackQuery, bot: Bot):
    await callback.answer()

    file = callback.message.document
    file_bytes_io = await bot.download(file)
    text_str = file_bytes_io.read().decode('utf-8')

    split_text = other_services.split_text(text_str)
    for chunk_text in split_text:
        await callback.message.answer(text=chunk_text)

    await callback.answer()


@router.message(F.text)
async def process_send_text_request_to_open_ai(message: Message, bot: Bot):
    answer = ai_service_curl.text_request_to_open_ai(text=message.text)
    await message.reply(text=answer)


@router.callback_query(Text(text=['send_text_open_ai']))
async def process_send_text_request_open_ai(callback: CallbackQuery, bot: Bot):
    await callback.answer()

    file = callback.message.document
    file_bytes_io = await bot.download(file)
    text_str = file_bytes_io.read().decode('utf-8')
    answer = ai_service_curl.text_request_to_open_ai(text=text_str)

    await callback.message.answer(text=answer)

