from aiogram.types import ReplyKeyboardMarkup, KeyboardButton       #, ReplyKeyboardRemove

b1 = KeyboardButton('/Оператора_Online')
b2 = KeyboardButton('/Где_заказать')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('/Оставить контакты', request_contact=True)
b5 = KeyboardButton('/Адрес доставки', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) #замещяем обычную клавиатуру на нашу с командами

kb_client.add(b1).add(b2).insert(b3).row(b4, b5) #добавляем кнопки из переменных. insert ставит кнопку по соседству(не переносит на другую строку)
#kb_clien.row(b1,b2,b3)     компановка кнопок по порядку