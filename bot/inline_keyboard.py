from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_NEKO = InlineKeyboardButton('Кошкодевочка', callback_data='neko')

NEKO = InlineKeyboardMarkup().add(BTN_NEKO)
