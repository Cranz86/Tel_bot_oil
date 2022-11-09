from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class FSMAdmin(StatesGroup):
    sts = State()
    dpf = State()
    oldoil = State()
    need = State()

#Страт диолога для запроса подбора масла
@dp.message.handler(commands='Подобрать масло', State=None)
async def cm_start(message : types.Message):
    await FSMAdmin.auto.set()
    await message.reply('Загрузите фото СТС')

#Ловим первый ответ от пользователя и записываем в базу
@dp.message_handler(content_types=['sts'], state=FSMAdmin.sts)
async def load_sts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:       #словарь хранения данных
        data['sts'] = message.photo[0].file_id     # присваеваем уникальный айди номер, для хранения в базе
    await FSMAdmin.next()       # переводим состояние бота в ожидание следующего ответа
    await message.reply('Сажевый фильтр (DPF) установлен?')

#Получаем второй ответ
@dp.message_handler(State=FSMAdmin.dpf)
async def load_dpf(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dpf'] = message.text
    await FSMAdmin.next()
    await message.reply('Какое масло использовали занее?')

#Получаем третий ответ
@dp.message_handler(State=FSMAdmin.oldoil)
async def load_oldoil(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['oldoil'] = message.text
    await FSMAdmin.next()
    await message.reply('Какое масло хотите сейчас?')

#Получаем четвертый ответ
@dp.message_handler(State=FSMAdmin.need)
async def load_need(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['need'] = message.text

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

#Регестрируем хендлеры
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Создать запрос'], State-None)
    dp.register_message_handler(load_sts, content_types=['sts'], state=FSMAdmin.sts)
    dp.register_message_handler(load_dpf, state=FSMAdmin.dpf)
    dp.register_message_handler(load_oldoil, state=FSMAdmin.oldoil)
    dp.register_message_handler(load_need, state=FSMAdmin.need)
