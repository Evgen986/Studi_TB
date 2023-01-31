from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_ID

bot = Bot(TOKEN_ID)
dp = Dispatcher(bot)
HELP_COMMANDS = """
<b>/start</b> - <i>Приветствие пользователя</i>
<b>/help</b> - <i>Список доступных команд</i>
<b>/картинка</b> - <i>Получить картинку</i>"""


async def on_start(_):
    print('Бот стартанул')


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
     await bot.send_message(message.from_user.id, HELP_COMMANDS, parse_mode='HTML')


@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(message.chat.id,
                         'https://media.istockphoto.com/id/104355461/ru/фото/вид-спереди-британская-американская-короткошёрстная-кошка-7-месяцев-сидя.jpg?s=612x612&w=0&k=20&c=tHDoLbkg2ESuqR6LiK_-GCPzqdlWaqr64mgTRRwdEz0=')
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(message.chat.id,
                            latitude=55,
                            longitude=78)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
