from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_ID
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text=' ', callback_data='b1')
b2 = InlineKeyboardButton(text=' ', callback_data='b2')
b3 = InlineKeyboardButton(text=' ', callback_data='b3')
b4 = InlineKeyboardButton(text=' ', callback_data='b4')
b5 = InlineKeyboardButton(text=' ', callback_data='b5')
b6 = InlineKeyboardButton(text=' ', callback_data='b6')
b7 = InlineKeyboardButton(text=' ', callback_data='b7')
b8 = InlineKeyboardButton(text=' ', callback_data='b8')
b9 = InlineKeyboardButton(text=' ', callback_data='b9')
ikb.add(b1, b2, b3).add(b4, b5, b6).add(b7, b8, b9)


async def on_start(_):
    print('Server start!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Давай играть!', reply_markup=ikb)


@dp.callback_query_handler()
async def but1_pressed(call: types.CallbackQuery):
    print(call)
    await call.answer(call.inline_message_id)


# @dp.callback_query_handler()
# async def call_command(callback: types.CallbackQuery):
#     if callback.data == 'b1':
#         global b1
#         b1 = InlineKeyboardButton('x', callback_data='b1')
#         await callback.answer('готово!')
#     await callback.answer('не прокатило')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
