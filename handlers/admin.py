from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filtres.state import State, StatesGroup
from aiogram import types

class FSMAdmin(StatesGroup):
    auto = State()
    dpf = State()
    oldoil = State()
    need = State()

#Страт диолога для запроса подбора масла
@dp.message.handler(commands='Подобрать масло', State=None)
async def cm_start(message : types.Message):
    await FSMAdmin.auto.set()
    await message.reply('Загрузите фото СТС')

#Ловим первый ответ от пользователя и записываем в базу
@dp.message_handler(content_types=['auto'], state=FSMAdmin.auto)
async def load_sts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['auto'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Сажевый фильтр (DPF) установлен?')
