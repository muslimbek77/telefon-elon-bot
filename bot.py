import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from config import BOT_TOKEN,ADMINS

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Salom, {full_name}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
