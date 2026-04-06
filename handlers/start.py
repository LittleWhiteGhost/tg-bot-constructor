"""
Обработчик команды /start
"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработка команды /start"""
    
    # Форматирование приветственного сообщения
    welcome_text = config.WELCOME_MESSAGE.format(
        name=message.from_user.first_name,
        bot_name=config.BOT_NAME
    )
    
    # Создание клавиатуры (если включено)
    if config.USE_INLINE_KEYBOARDS:
        kb = InlineKeyboardBuilder()
        kb.button(text="📋 Помощь", callback_data="help")
        kb.button(text="ℹ️ О боте", callback_data="about")
        kb.button(text="⚙️ Настройки", callback_data="settings")
        kb.adjust(2)
        
        await message.answer(welcome_text, reply_markup=kb.as_markup())
    else:
        await message.answer(welcome_text)
