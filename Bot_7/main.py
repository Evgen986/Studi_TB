from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN_ID

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)

ikey = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton('мыло.ру', url='https://mail.ru/')
ib2 = InlineKeyboardButton('шмяндекс.ру', url='https://ya.ru/')
ikey.add(ib1, ib2)


async def on_start(_):
    print('Бот запущен!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello World!', reply_markup=ikey)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
