from aiogram import Router
from aiogram.filters import Text, Command
from aiogram.types import Message
from telegram.keyboards import main_btns
from aiogram.filters import Text, Command

main_router = Router()


@main_router.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer("Вітаємо, ми вам допоможемо!",
                         reply_markup=main_btns)
