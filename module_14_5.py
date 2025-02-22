from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions_m14_5 import *


all_products = get_all_products()


api = ''
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())



kb = ReplyKeyboardMarkup(resize_keyboard=True)

button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
button_4 = KeyboardButton(text='Регистрация')

kb.row(button_1, button_2)
kb.add(button_3, button_4)


kb_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
])


kb_inline_prod = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=f'{all_products[0][1]}', callback_data='product_buying'),
        InlineKeyboardButton(text=f'{all_products[1][1]}', callback_data='product_buying'),
        InlineKeyboardButton(text=f'{all_products[2][1]}', callback_data='product_buying'),
        InlineKeyboardButton(text=f'{all_products[3][1]}', callback_data='product_buying')
    ]
])



class UserState(StatesGroup):

    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):

    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот, который сможет подсчитать вашу норму калорий.')


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in get_all_products():
        await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        with open(f'img_{i[0]}.jpg', 'rb') as img:
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


# __________Машина состояний (расчет калорий)_____________________________________________________

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
# ________________________________________________________________________________________________

# __________Машина состояний (регистрация)________________________________________________________

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит)')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя')
        return
    await state.update_data(k_username=message.text)
    await message.answer('Введите свой email:')
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(k_email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(k_age=message.text)
    user_data = await state.get_data()
    user_data = list(user_data.values())
    add_user(user_data[0], user_data[1], user_data[2])
    await message.answer('Регистрация прошла успешно')
    await state.finish()
# ________________________________________________________________________________________________


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
