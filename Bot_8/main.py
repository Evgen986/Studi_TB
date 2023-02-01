from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_ID
from IKeyboard import ikb
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/links')
kb.add(b1)


async def on_start(_):
    print('Я запустился!')


@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await message.answer('Выбери вариант:', reply_markup=ikb)


@dp.message_handler()
async def unknown_command(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEHijdj2jpoePppDQ-ye4hVXVIGBehfFAACByYAArCAgEqLpTHeB5NBWy4E')
    await message.answer('Я не знаю такого слова', reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
