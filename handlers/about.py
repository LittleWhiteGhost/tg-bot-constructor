"""
Обработчик команды /about
"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import config

router = Router()


@router.message(Command("about"))
async def cmd_about(message: Message):
    """Обработка команды /about"""
    
    # Форматирование сообщения о боте
    about_text = config.ABOUT_MESSAGE.format(
        bot_name=config.BOT_NAME,
        version=config.VERSION,
        author=config.AUTHOR,
        description=config.BOT_DESCRIPTION
    )
    
    await message.answer(about_text)


@router.callback_query(F.data == "about")
async def callback_about(callback: CallbackQuery):
    """Обработка callback кнопки о боте"""
    
    about_text = config.ABOUT_MESSAGE.format(
        bot_name=config.BOT_NAME,
        version=config.VERSION,
        author=config.AUTHOR,
        description=config.BOT_DESCRIPTION
    )
    
    await callback.message.edit_text(about_text)
    await callback.answer()
