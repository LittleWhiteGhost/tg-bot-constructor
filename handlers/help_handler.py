"""
Обработчик команды /help
"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import config

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработка команды /help"""
    
    # Формирование списка команд
    commands_list = "\n".join([
        f"/{cmd} — {desc}"
        for cmd, desc in config.COMMANDS.items()
    ])
    
    # Форматирование сообщения помощи
    help_text = config.HELP_MESSAGE.format(
        commands_list=commands_list
    )
    
    await message.answer(help_text)


@router.callback_query(F.data == "help")
async def callback_help(callback: CallbackQuery):
    """Обработка callback кнопки помощи"""
    
    commands_list = "\n".join([
        f"/{cmd} — {desc}"
        for cmd, desc in config.COMMANDS.items()
    ])
    
    help_text = config.HELP_MESSAGE.format(
        commands_list=commands_list
    )
    
    await callback.message.edit_text(help_text)
    await callback.answer()
