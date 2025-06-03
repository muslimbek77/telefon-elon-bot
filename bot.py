import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from config import BOT_TOKEN,ADMINS
from keyboard_buttons import menu_button
from aiogram.fsm.context import FSMContext
from mystate import Elon

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Salom, {full_name}",reply_markup=menu_button)

@dp.message(F.text == "📢 Elon berish")
async def elon_post(message: types.Message,state: FSMContext):
    await message.answer("Telefon modeli va nomini kiring...")
    await state.set_state(Elon.phone_model)

@dp.message(F.text,Elon.phone_model)
async def elon_model(message: types.Message,state: FSMContext):
    ph_model = message.text
    await state.update_data(phone_model = ph_model)
    await message.answer("Rasmini yuboring..")
    await state.set_state(Elon.image)

@dp.message(F.photo,Elon.image)
async def elon_image(message: types.Message,state: FSMContext):
    img = message.photo[-1].file_id

    await state.update_data(image = img)
    await message.answer("Telefon narxini kiriting...")
    await state.set_state(Elon.price)

@dp.message(F.text,Elon.price)
async def elon_price(message: types.Message,state: FSMContext):
    price = message.text
    await state.update_data(price = price)
    await message.answer("Telefon malumotizni qoldiring..")
    await state.set_state(Elon.phone_number)

@dp.message(F.text,Elon.phone_number)
async def elon_phone_number(message: types.Message,state: FSMContext):
    data = await state.get_data()
    phone_model = data.get("phone_model")
    image = data.get("image")
    price = data.get("price")
    phone_number = message.text
    text = f"Model: {phone_model}\nNarxi: {price}\n Murojaat uchun tel: {phone_number}"
    await message.answer_photo(photo=image,caption=text,reply_markup=menu_button)
 
    await state.clear()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
