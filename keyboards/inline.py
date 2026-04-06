"""
Inline клавиатуры
"""

from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    """Главное меню"""
    kb = InlineKeyboardBuilder()
    kb.button(text="📋 Помощь", callback_data="help")
    kb.button(text="ℹ️ О боте", callback_data="about")
    kb.button(text="⚙️ Настройки", callback_data="settings")
    kb.adjust(2)
    return kb.as_markup()


def yes_no_keyboard(yes_data="yes", no_data="no"):
    """Клавиатура Да/Нет"""
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ Да", callback_data=yes_data)
    kb.button(text="❌ Нет", callback_data=no_data)
    kb.adjust(2)
    return kb.as_markup()


def back_button(callback_data="back"):
    """Кнопка назад"""
    kb = InlineKeyboardBuilder()
    kb.button(text="◀️ Назад", callback_data=callback_data)
    return kb.as_markup()


def url_button(text, url):
    """Кнопка с URL"""
    kb = InlineKeyboardBuilder()
    kb.button(text=text, url=url)
    return kb.as_markup()


def custom_keyboard(buttons_data):
    """
    Создание кастомной клавиатуры
    
    buttons_data = [
        {"text": "Кнопка 1", "callback_data": "btn1"},
        {"text": "Кнопка 2", "callback_data": "btn2"},
    ]
    """
    kb = InlineKeyboardBuilder()
    for btn in buttons_data:
        if "url" in btn:
            kb.button(text=btn["text"], url=btn["url"])
        else:
            kb.button(text=btn["text"], callback_data=btn["callback_data"])
    kb.adjust(2)
    return kb.as_markup()
