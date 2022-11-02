from cgitb import text
from email import message_from_file

from aiogram.utils import executor
from create_bot import dp





async def on_startup(_):        #проверка действий бота в командной строке
    print('Бот вышел в онлайн')     #текст в логах
from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)       #важно импортировать последним, что бы работали команды (echo)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)    #skip_updates=True пропускаем сообщение которые пришли в офлайне