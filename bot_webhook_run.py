from aiogram import Dispatcher, Bot, types, filters, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, Text
from config_data.config import BOT_TOKEN


from aiohttp import web


bot = Bot(token=BOT_TOKEN)

Bot.set_current(bot)

dp = Dispatcher()
app = web.Application()

webhook_path = f'/{BOT_TOKEN}'


async def set_webhook():
    webhook_uri = f'https://5482-212-58-114-216.eu.ngrok.io{webhook_path}'
    await bot.set_webhook(webhook_uri)


async def on_startup(_):
    await set_webhook()


@dp.message(CommandStart())
async def command_start_help(message: types.Message) -> None:
    await message.answer(text='Hello Human🤖🌿℃')


@dp.message(F.text)
async def audio(message: types.Message) -> None:
    await message.answer(text="La La Text 🕋")


@dp.message(F.voice)
async def audio(message: types.Message) -> None:
    await message.answer(text="La La Voice 🕋")


@dp.message(F.audio)
async def audio(message: Message) -> None:
    await message.answer(text="La La Audio 🕋")


@dp.message(F.document)
async def audio(message: types.Message) -> None:
    await message.answer(text="La La Document 🕋")


async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[index + 1:]

    if token == BOT_TOKEN:
        request_data = await request.json()
        # update = types.Update(**request_data)

        await dp.feed_raw_update(bot, request_data)  # Main entry point for incoming updates with automatic Dict

        print(request_data)
        return web.Response()
    else:
        web.Response(status=403)


app.router.add_post(f'/{BOT_TOKEN}', handle_webhook)  # Shortcut for add_route with method POST

if __name__ == '__main__':
    app.on_startup.append(on_startup)

    web.run_app(
        app,
        host='0.0.0.0',
        port=8080,
    )
