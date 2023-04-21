import logging
import configparser
import inline_keyboard
import messages

from aiogram import Bot, executor, Dispatcher, types

# подключаем конфиг, лог и инициализируем бота
config = configparser.ConfigParser()
config.read('../config.ini')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config['telegram']['token'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(text=messages.start(), reply_markup=inline_keyboard.NEKO)


@dp.callback_query_handler(text='neko')
async def process_callback_neko(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_reply_markup()
    await bot.send_photo(callback_query.from_user.id,
                         photo=messages.neko_pic(),
                         caption=messages.neko(),
                         reply_markup=inline_keyboard.NEKO)


executor.start_polling(dp, skip_updates=True)
