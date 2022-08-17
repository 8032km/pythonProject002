import asyncio
from asyncio import sleep
from random import choice

from aiogram import Bot, Dispatcher, executor, types

bot = Bot('')

dp = Dispatcher(bot)

games = {'chat_id':
             {'users': ['username1', '2'], 'm_id': 123}
         }


@dp.message_handler(commands=['start'])
async def func(message: types.Message):
    if message.chat.id in games:
        await bot.send_message(message.chat.id, 'Игра уже начата')
    else:
        m = types.InlineKeyboardMarkup()
        m.add(types.InlineKeyboardButton('Join', callback_data='join'))
        msg = await bot.send_message(message.chat.id, 'Ждем игроков! уже 0 готовы!', reply_markup=m)
        games[message.chat.id] = {'users': [], 'msg': msg}
        await sleep(60)
        if message.chat.id in games:
            games.pop(message.chat.id)
            await bot.send_message(message.chat.id, 'Не успели набрать нужное кол-во играков')
            await bot.delete_message(msg.chat.id, msg.message_id)


@dp.callback_query_handler(lambda call: call.data == 'join')
async def join(call: types.CallbackQuery):
    if call.message.chat.id in games:
        msg = games[call.message.chat.id]['msg']
        if call.message.message_id == msg.message_id:
            users_list = games[call.message.chat.id]['users']
            if call.from_user.id not in users_list:
                users_list.append(call.from_user.username)
                await bot.edit_message_text(f'Ждем игроков! уже {len(users_list)} готовы!', msg.chat.id, msg.message_id,
                                            reply_markup=msg.reply_markup)
                if len(users_list) >= 3:
                    games.pop(msg.chat.id)
                    await bot.send_message(msg.chat.id, 'Игра начата!')
                    await bot.delete_message(msg.chat.id, msg.message_id)
                    await sleep(1)
                    await bot.send_message(msg.chat.id, '3')
                    await sleep(1)
                    await bot.send_message(msg.chat.id, '2')
                    await sleep(1)
                    await bot.send_message(msg.chat.id, '1')
                    await sleep(1)
                    await bot.send_message(msg.chat.id, f'Победил {choice(users_list)}')


executor.start_polling(dp)

'''
Создать бота, у которого есть команда play,
после того как вы нажмете /play, бот выведет окошко присоеденится.
Если игра уже запущена, то бот не даст создать еще одну в одном и том же чате.

Бот ждет пока к игре присоеденится 3 человека.
"""Ждем игроков
   присоеденится
"""
После того как 3 игрока присоеденится
-> игра Началась
через 2 секунды начнет обратный отсчет
->3
->2
->1
-> имя игрока который победил

Если проходит 1 минута, и никто не присоединяется, то бот говорит что набралось недостаточно игроков
'''
