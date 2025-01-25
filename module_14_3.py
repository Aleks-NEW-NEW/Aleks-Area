from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = ''
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())



kb = ReplyKeyboardMarkup(resize_keyboard=True)

button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')

kb.row(button_1, button_2)
kb.add(button_3)


kb_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
])


products_names = ['Батончик', 'Протеин', 'Креатин', 'BCAA']

kb_inline_prod = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=f'{products_names[0]}', callback_data='product_buying'),
        InlineKeyboardButton(text=f'{products_names[1]}', callback_data='product_buying'),
        InlineKeyboardButton(text=f'{products_names[2]}', callback_data='product_buying'),
        InlineKeyboardButton(text=f'{products_names[3]}', callback_data='product_buying')
    ]
])



class UserState(StatesGroup):

    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот, который сможет подсчитать вашу норму калорий.')


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i, name in enumerate(products_names, start=1):
        await message.answer(f'Название: {name} | Описание: описание {i} | Цена: {i * 100}')
        with open(f'img_{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer(f'Выберите продукт для покупки:', reply_markup=kb_inline_prod)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес(кг) + 6,25 х рост(см) - 5 х возраст(г) - 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        if isinstance(float(message.text), (int, float)):
            await state.update_data(k_age=message.text)
            await message.answer('Введите свой рост:')
            await UserState.growth.set()
    except ValueError:
        await message.answer('Значение возраста должно быть числом!\nПопробуйте снова.')
        return


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        if isinstance(float(message.text), (int, float)):
            await state.update_data(k_growth=message.text)
            await message.answer('Введите свой вес:')
            await UserState.weight.set()
    except ValueError:
        await message.answer('Значение роста должно быть числом!\nПопробуйте снова.')
        return


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    try:
        if isinstance(float(message.text), (int, float)):
            await state.update_data(k_weight=message.text)
            data = await state.get_data()
            calories_amount = ((10 * float(data['k_weight'])) + (6.25 * float(data['k_growth']))
                               - (5 * float(data['k_age'])) - 161)
            await message.answer(f'Ваша норма калорий: {calories_amount}')
            await state.finish()
    except ValueError:
        await message.answer('Значение веса должно быть числом!\nПопробуйте снова.')
        return


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
