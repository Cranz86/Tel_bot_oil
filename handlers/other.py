'''ОБЩАЯ ЧАСТЬ'''

from aiogram import types, Dispatcher
from create_bot import dp
import json, string

#@dp.message_handler()    #декоратор события написания в чат
async def echo_send(message : types.Message):    #асинхронная функция ловит любые текстовые сообщения
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Матетирся запрещено!')
        await message.delete()
#lower перевод в нижний регистр
#string.punctuation - список всех знаков препинания, которые убираем из завуальрованного мата "жо!па"

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)



    #if message.text == 'Привет':
        #await message.answer('Добрый вечер!')

    #await message.answer(message.text)      #Способ №1: из потока ждём сообщение и отправляем ответ
    #await message.reply(message.text)        #Способ №2: с упоминание сообщения на которое отвечает бот (цитирование)
    #await bot.send_message(message.from_user.id, message.text)      ##Способ №3: отправить сообщение в личку, сработает если пользователь писал боту ранее
    