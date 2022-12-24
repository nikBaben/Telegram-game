from aiogram import Bot, Dispatcher, executor, types
from data import create_db,create_profile

API_TOKEN = '5801245073:AAE8sJPIIVhz88j1tV-WRDQEG6ZV27x_mCM'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def start(_): 
    await create_db()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет")
    user_id = message.from_user.id
    await create_profile(user_id = user_id)





if __name__ == "__main__":
     executor.start_polling(dp, skip_updates=True,on_startup=start)