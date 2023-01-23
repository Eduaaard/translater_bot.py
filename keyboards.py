from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import LANGCODES


def show_start_menu(chat_id: int | None = None):
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True)

    mark_up.row(
        KeyboardButton(text='Регистрация')
    )

    mark_up.row(
        KeyboardButton(text='Перевод'),
        KeyboardButton(text='История перевода'),
    )
    return mark_up


def show_lang_menu():

    mark_up = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    mark_up.row(
        KeyboardButton(text='Назад')
    )

    buttons = [KeyboardButton(text=lang) for lang in LANGCODES.keys()]
    mark_up.add(*buttons)
    return mark_up

def contact_button():
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True)

    mark_up.row(
        KeyboardButton(text='Отправить контакт', request_contact=True)
    )
    return mark_up


