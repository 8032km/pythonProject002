from aiogram import Bot, Dispatcher, executor, types
from asyncio import sleep

token = ''

bot = Bot(token)

dp = Dispatcher(bot)


@dp.message_handler()
async def func(message: types.Message):
    for i in range(10):
        await bot.send_message(message.chat.id, str(i))
        await sleep(1)


executor.start_polling(dp)
