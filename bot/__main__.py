from bot import settings
from bot import services
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from bot.handlers import routers

logger = logging.getLogger(__name__)
bot = Bot(token=settings.TOKEN)


async def main():
    storage = MemoryStorage()
    services.setup_logging()
    dp = Dispatcher(storage=storage)
    for router in routers:
        dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    logger.debug("handlers configured successfully")
    logger.info("started")
    try:
        await dp.start_polling(bot)
    finally:
        logger.info("stopped")


def cli():
    asyncio.run(main())
