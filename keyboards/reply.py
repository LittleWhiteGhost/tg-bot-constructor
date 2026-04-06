"""
Reply клавиатуры
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_reply():
    """Главное меню (reply)"""
    kb = ReplyKeyboardBuilder()
    kb.button(text="📋 Помощь")
    kb.button(text="ℹ️ О боте")
    kb.button(text="⚙️ Настройки")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def remove_keyboard():
    """Удалить клавиатуру"""
    from aiogram.types import ReplyKeyboardRemove
    return ReplyKeyboardRemove()


def contact_keyboard():
    """Клавиатура для запроса контакта"""
    kb = ReplyKeyboardBuilder()
    kb.button(text="📱 Отправить контакт", request_contact=True)
    return kb.as_markup(resize_keyboard=True)


def location_keyboard():
    """Клавиатура для запроса геолокации"""
    kb = ReplyKeyboardBuilder()
    kb.button(text="📍 Отправить геолокацию", request_location=True)
    return kb.as_markup(resize_keyboard=True)


def custom_reply_keyboard(buttons):
    """
    Создание кастомной reply клавиатуры
    
    buttons = ["Кнопка 1", "Кнопка 2", "Кнопка 3"]
    """
    kb = ReplyKeyboardBuilder()
    for btn in buttons:
        kb.button(text=btn)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
