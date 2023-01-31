from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_ID

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)


async def on_start(_):
    print('Я запустился!')


@dp.message_handler(content_types=['sticker'])
async def id_stickers(message: types.Message):
    await message.reply(message.sticker.file_id)


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer('Смотри какой смешной кот' + '❤️')
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEHhyhj2Q3G8_LnmlZTrKD5asKpoCTTjQACGCMAAu0HgUrqmupuzpQQ6y0E')
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('<b>give</b> - <i>получить сердечко</i>\n'
                         '<b>help</b> - <i>получить список команд</i>', parse_mode='HTML')
    await message.delete()


@dp.message_handler()
async def send_heart(message: types.Message):
    if '❤️' in message.text:
        await message.answer('🖤')
    elif '✅' in message.text:
        await message.answer(f'В тексте {message.text.count("✅")} символов ✅')



# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.answer('<em><b>Здорово!</b></em>', parse_mode='HTML')
#
#
# @dp.message_handler(commands=['give'])
# async def get_sticker(message: types.Message):
#     await bot.send_sticker(message.chat.id,
#                            sticker='CAACAgIAAxkBAAEHhyhj2Q3G8_LnmlZTrKD5asKpoCTTjQACGCMAAu0HgUrqmupuzpQQ6y0E')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
