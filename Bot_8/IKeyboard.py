from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton('мыло', url='https://mail.ru/')
ib2 = InlineKeyboardButton('шмяндекс', url='https://yandex.ru/')
ikb.add(ib1, ib2)
