from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_ID
from random import randint

DESCRIPTION_BOT = """
Это простой и самый обыкновенный тренировочный бот,
который ни чего не умеет!"""

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)
count = 0


@dp.message_handler(commands=['count'])
async def count_calls(message: types.Message):
    global count
    count += 1
    await message.reply(f'Меня вызывали {count} раз!')


@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.answer(DESCRIPTION_BOT)
    await message.delete()


@dp.message_handler()
async def answer(message: types.Message):
    if '0' in message.text:
        await message.reply('YES')
    else:
        await message.reply('NO')


@dp.message_handler()
async def random_ch(message: types.Message):
    await message.answer(chr(randint(97, 122)))


if __name__ == '__main__':
    executor.start_polling(dp)