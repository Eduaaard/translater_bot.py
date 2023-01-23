from telebot import TeleBot
from telebot.types import Message
import keyboards as kb
from googletrans import Translator, LANGCODES

translator = Translator()

BOT_TOKEN = '5594403804:AAEQRAisGkTGM5IebvVvlT794xCCYqCZMC8'

bot = TeleBot(token=BOT_TOKEN)


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
    bot.send_message(chat_id, 'Напишите Ф.И.О')
    bot.register_next_step_handler(message, get_full_name)


def get_full_name(message: Message):
    chat_id = message.chat.id
    full_name = message.text.title()
    bot.send_message(chat_id, "Отправьте ваш контакт", reply_markup=kb.contact_button())
    bot.register_next_step_handler(message, register_user, full_name)


def register_user(message: Message, full_name: str):
    chat_id = message.chat.id
    print(message.contact.phone_number, full_name)
    bot.send_message(chat_id, "Регистрация прошла успешно", reply_markup=kb.show_start_menu())

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
    chat_id = message.chat.id
    lang_code_from = LANGCODES[lang_from]
    lang_code_for = LANGCODES[lang_for]

    translated_text = translator.translate(message.text, dest=lang_code_for, src=lang_code_from).text
    bot.send_message(chat_id, f"""
Переведено с : {lang_from.title()}
Переведено на : {lang_for.title()}
Оригинал : {message.text}
Перевод : {translated_text}
""", reply_markup=kb.show_start_menu())
    # return translated_text

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@bot.message_handler(func=lambda msg: msg.text == 'История перевода')
def for_history_translate_button(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Действие история перевода запущена')
    # translated_text = translate_message()


@bot.message_handler(func=lambda msg: msg.text == 'Назад')
def for_back(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Назад так назад', reply_markup=kb.show_start_menu())


# -------------------------------------------------------------------------


bot.infinity_polling()
