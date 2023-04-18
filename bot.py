import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import admin_handlers, user_handlers, other_handlers

from config_data.config import OPENAI_API_KEY, OPENAI_API_KEY_FROM_HRY, BOT_TOKEN, ADMIN_IDS
from services import ai_service

# Logger initialise
logger = logging.getLogger(__name__)


# Function for configure and run Bot
async def main():
    # configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Write to console info about bot start
    logger.info("Starting bot")

    # Initialise Bot and Dispatcher
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Register routers in Dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Pass all updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
