from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


api = ''
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())



class UserState(StatesGroup):

    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        if isinstance(int(message.text), int):
            await state.update_data(k_age=message.text)
            await message.answer('Введите свой рост:')
            await UserState.growth.set()
    except ValueError:
        await message.answer('Значение возраста должно быть числом!\nПопробуйте снова.')
        return


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        if isinstance(int(message.text), int):
            await state.update_data(k_growth=message.text)
            await message.answer('Введите свой вес:')
            await UserState.weight.set()
    except ValueError:
        await message.answer('Значение роста должно быть числом!\nПопробуйте снова.')
        return


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    try:
        if isinstance(int(message.text), int):
            await state.update_data(k_weight=message.text)
            data = await state.get_data()
            calories_amount = (10 * int(data['k_weight'])) + (6.25 * int(data['k_growth'])) - (5 * int(data['k_age'])) + 5
            await message.answer(f'Ваша норма калорий: {calories_amount}')
            await state.finish()
    except ValueError:
        await message.answer('Значение веса должно быть числом!\nПопробуйте снова.')
        return


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
