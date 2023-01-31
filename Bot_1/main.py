from aiogram import Bot, Dispatcher, executor, types


TOKEN_ID = '5841865362:AAGe-mekNEv9gYIPrV8kxAA6eNihfpSGJrU'
bot = Bot(TOKEN_ID)
dip = Dispatcher(bot)


@dip.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)  # Написать сообщение с текстом
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dip)
