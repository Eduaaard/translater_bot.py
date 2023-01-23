from telebot import TeleBot
from telebot.types import Message
import keyboards as kb

BOT_TOKEN = '5594403804:AAEQRAisGkTGM5IebvVvlT794xCCYqCZMC8'

bot = TeleBot(token=BOT_TOKEN)
git = g


# -------------------------------------------------------------------------

@bot.message_handler(commands=["start"])
def command_start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    bot.send_message(chat_id, f'''Hello, {first_name}
your username is @{username}''', reply_markup=kb.show_start_menu())


@bot.message_handler(func=lambda msg: msg.text == 'Назад')
def for_back(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Назад так назад', reply_markup=kb.show_start_menu())


# -------------------------------------------------------------------------


@bot.message_handler(func=lambda msg: msg.text == 'Регистрация')
def for_registration_button(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Действие регистрация запущена')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.message_handler(func=lambda msg: msg.text == 'Перевод')
def for_translate_button(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите язык с которого будем переводить', reply_markup=kb.show_lang_menu())
    bot.register_next_step_handler(message, get_lang_from)


def get_lang_from(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите язык на который будем переводить', reply_markup=kb.show_lang_menu())
    bot.register_next_step_handler(message, get_lang_for_translate, message.text)


def get_lang_for_translate(message: Message, lang_from: str):
    chat_id = message.chat.id
    # print(message.text, lang_from)
    bot.send_message(chat_id, 'Напишите слово или текст для перевода')
    bot.register_next_step_handler(message, translate_message, lang_from, message.text)


def translate_message(message: Message, lang_from: str, lang_for: str):
    print(f'Слово {message.text}, с {lang_from} на {lang_for}')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@bot.message_handler(func=lambda msg: msg.text == 'История перевода')
def for_history_translate_button(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Действие история перевода запущена')


@bot.message_handler(func=lambda msg: msg.text == 'Назад')
def for_back(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Назад так назад', reply_markup=kb.show_start_menu())


# -------------------------------------------------------------------------


bot.infinity_polling()
