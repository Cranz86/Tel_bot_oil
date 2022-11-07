from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Оператора_Online')
b2 = KeyboardButton('/Где_заказать')
b3 = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup() #замещяем обычную клавиатуру на нашу с командами

kb_client.add(b1).add(b2).add(b3) #добавляем кнопки из переменных