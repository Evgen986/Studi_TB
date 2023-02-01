from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_ID
from random import randint

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)
chat_id = ''

HELP_MES = """
<b>/help</b> - <i>список команд</i>
<b>/description</b> - <i>описание бота</i>"""

kb_unknown = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/❤️')
b4 = KeyboardButton('/location')
kb_unknown.add(b1).insert(b2).add(b3).insert(b4)

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
but_1 = KeyboardButton('/help')
but_2 = KeyboardButton('/orange')
but_3 = KeyboardButton('/location')
kb_start.add(but_1).insert(but_2).insert(but_3)


async def on_start(_):
    print('Бот запущен!')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(HELP_MES, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def des_command(message: types.Message):
    await message.answer('Это самый простой бот!')
    await message.delete()


@dp.message_handler(commands=['❤️'])
async def answer_heart(message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHijtj2ju25yD9IASXu2icS_RIgMtu1AAClygAAhcXgEq2a7UNPA1jui4E')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(message.from_user.id, 'q', reply_markup=kb_start)
    await message.delete()


@dp.message_handler(commands=['orange'])
async def send_orange(message: types.Message):
    await bot.send_photo(chat_id,
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVDneRTKcg1yAALTzN90PM1MIkFz_NnK16Iw&usqp=CAU')
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_loc(message: types.Message):
    await bot.send_location(message.chat.id, latitude=randint(1, 100), longitude=randint(1, 100) )
    await message.delete()


@dp.message_handler()
async def unknown_message(message: types.Message):
    await bot.send_sticker(message.chat.id,
                           'CAACAgIAAxkBAAEHijdj2jpoePppDQ-ye4hVXVIGBehfFAACByYAArCAgEqLpTHeB5NBWy4E',
                           reply_markup=kb_unknown)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)