'''КЛИЕНТСКАЯ ЧАСТЬ''' #т.к. пришем в одном файте, разбиваем его на блоки

from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start', 'help'])     #обязательные команды для бота
async def command_start(message : types.Message):
    try:        #Обрабатывает ошибку, если пользователь ранее не писал боту
        await  bot.send_message(message.from_user.id, 'Подберём Вам масло?', reply_markup=kb_client)
        await message.delete()      #чистим после ошибки
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Oil_supportBot')

#@dp.message_handler(commands=['Оператора_Online'])
async def oil_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'С 9:00 до 21:00, Пн.-Пт.')

#@dp.message_handler(commands=['Где_заказать'])
async def oil_bay_comand(message : types.Message):
    await bot.send_message(message.from_user.id, 'Маркетплейсы: Сбер, Яндекс, OZON, WB', reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])      #вместо декоратора обязательных команд
    dp.register_message_handler(oil_open_command, commands=['Оператора_Online'])
    dp.register_message_handler(oil_bay_comand, commands=['Где_заказать'])