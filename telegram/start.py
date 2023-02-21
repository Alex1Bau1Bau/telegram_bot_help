from aiogram import Dispatcher
from telegram.setup import bot
from telegram.handlers import fsm_router, main_router


async def start_bot():
    dp = Dispatcher()
    dp.include_router(fsm_router)
    dp.include_router(main_router)
    await dp.start_polling(bot)

