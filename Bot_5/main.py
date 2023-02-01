from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_ID
from random import choice

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/start</b> - <i>запускает бота</i>
<b>/help</b> - <i>список команд</i>
<b>/description</b> - <i>описание бота</i>
<b>/photo</b> - <i>присылает фотографию</i>"""


PHOTO_URL = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRruSumTX7k1YAJV_DXZfvznmj5cZL3pYXbcw&usqp=CAU',
             'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVzX9qO7LHJgPgf_WvLq98IAa1FWyYPwRETg&usqp=CAU',
             'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCZdSKCzv3agIyMwHmqlWxJRDneAhfVgEnow&usqp=CAU',
             'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSukRnBurrT7JR-wG-rV0tW7yihcS5SNIFAEQ&usqp=CAU']

kb_help = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/description')
b2 = KeyboardButton('/photo')
kb_help.add(b1).insert(b2)

async def on_start(_):
    print('Бот запустился!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           'CAACAgIAAxkBAAEHhyhj2Q3G8_LnmlZTrKD5asKpoCTTjQACGCMAAu0HgUrqmupuzpQQ6y0E',)
    await bot.send_message(message.from_user.id, 'Я запустился!')
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, HELP_COMMAND, parse_mode='HTML', reply_markup=kb_help)
    await message.delete()


@dp.message_handler(commands=['description'])
async def des_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Я бот, который умеет отправлять картинки')
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.chat.id, choice(PHOTO_URL))
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
