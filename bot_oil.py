from cgitb import text
from email import message_from_file
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, json, string

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):        #проверка действий бота в командной строке
    print('Бот вышел в онлайн')     #текст в логах

'''КЛИЕНТСКАЯ ЧАСТЬ''' #т.к. пришем в одном файте, разбиваем его на блоки
@dp.message_handler(commands=['start', 'help'])     #обязательные команды для бота
async def command_start(message : types.Message):
    try:        #Обрабатывает ошибку, если пользователь ранее не писал боту
        await  bot.send_message(message.from_user.id, 'Подберём Вам масло?')
        await message.delete()      #чистим после ошибки
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Oil_supportBot')

@dp.message_handler(commands=['Режим оператора Online'])
async def oil_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'С 9:00 до 21:00, Пн.-Пт.')

@dp.message_handler(commands=['Где заказать'])
async def oil_bay_comand(message : types.Message):
    await bot.send_message(message.from_user.id, 'Маркетплейсы: Сбер, Яндекс, OZON, WB')

'''АДМИНСКАЯ ЧАСТЬ'''

'''ОБЩАЯ ЧАСТЬ'''

@dp.message_handler()    #декоратор события написания в чат
async def echo_send(message : types.Message):    #асинхронная функция ловит любые текстовые сообщения
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Матетирся запрещено!')
        await message.delete()
#lower перевод в нижний регистр
#string.punctuation - список всех знаков препинания, которые убираем из завуальрованного мата "жо!па"


    #if message.text == 'Привет':
        #await message.answer('Добрый вечер!')

    #await message.answer(message.text)      #Способ №1: из потока ждём сообщение и отправляем ответ
    #await message.reply(message.text)        #Способ №2: с упоминание сообщения на которое отвечает бот (цитирование)
    #await bot.send_message(message.from_user.id, message.text)      ##Способ №3: отправить сообщение в личку, сработает если пользователь писал боту ранее
    
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)    #skip_updates=True пропускаем сообщение которые пришли в офлайне