from aiogram import Bot, Dispatcher, executor, types
from data import create_db,create_profile,get_user,get_balance,up_balance,get_start,update_start
from datetime import datetime
from threading import Timer
import asyncio
import time
from aio_timers import Timer
from threading import *
from multiprocessing import Process


API_TOKEN = '5978814839:AAHYphqvVnPtFq2bIr2NfqRbJ9xfYC8U65g'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def start(_): 
    await create_db()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print(user_name)
    await create_profile(user_id = user_id,user_name = user_name)
    a = await get_user(user_id = user_id)
    await message.answer(f"Привет {a[0]} ")


@dp.message_handler(commands=['start_gmae'])
async def send_welcome(message: types.Message):
    a = await get_balance(message.from_user.id)
    async def Task():
      while True:
        a = await get_balance(user_id = message.from_user.id)
        b = a[0]
        await asyncio.sleep(2)
        b +=1 
        await up_balance(money = b,user_id = message.from_user.id)
        print(b)
        print(await get_start(user_id = message.from_user.id))
    start = await get_start(user_id = message.from_user.id)
    if start[0]==0: 
        await update_start(flag = 1,user_id= message.from_user.id)
        await message.answer("Игра Началась, каждую секунду вам будут начисляться монеты")
        await Task()
    if start[0] == 1: 
        await message.answer("вы не можете начать игру 2 раза!")
    

@dp.message_handler(commands=['balance'])
async def send_welcome(message: types.Message):
    a = await get_balance(user_id = message.from_user.id)
    await message.answer(f"ВАШ БАЛАНС - {a[0]}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True,on_startup=start)
    t1 = Process(target = send_welcome)
    t1.start()
    t1.join()