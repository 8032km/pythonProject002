from aiogram import Bot, Dispatcher, executor, types

token = ''

bot = Bot(token)

dp = Dispatcher(bot)


@dp.message_handler()
async def func(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


executor.start_polling(dp)
