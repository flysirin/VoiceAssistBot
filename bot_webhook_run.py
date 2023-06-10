import asyncio

from aiogram import Dispatcher, Bot
from config_data.config import BOT_TOKEN, WEBHOOK_URL
from handlers import user_handlers  # , other_handlers

from aiohttp import web
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
Bot.set_current(bot)

dp = Dispatcher()
app = web.Application()

webhook_path = f'/{BOT_TOKEN}'
webhook_url = f'{WEBHOOK_URL}{webhook_path}'

# Register routers in Dispatcher
dp.include_router(user_handlers.router)


async def set_webhook():
    await bot.set_webhook(webhook_url, drop_pending_updates=True)


async def on_startup(_):
    await set_webhook()


async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[index + 1:]

    if token == BOT_TOKEN:
        request_data = await request.json()
        logger.warning(request_data)

        # Start processing in the background mode, not block main process
        # Main entry point for incoming updates with automatic Dict
        asyncio.create_task(dp.feed_raw_update(bot, request_data))

        return web.Response()
    else:
        web.Response(status=403)


app.router.add_post(webhook_path, handle_webhook)  # Shortcut for add_route with method POST

if __name__ == '__main__':
    app.on_startup.append(on_startup)
    logger.warning("Start Bot")

    web.run_app(
        app,
        host='0.0.0.0',
        port=8080,
    )

    logger.warning('END BOT')
