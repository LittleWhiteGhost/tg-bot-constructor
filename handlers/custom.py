"""
Кастомные обработчики - добавь свои команды здесь!
"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


# ============================================
# ПРИМЕР 1: Простая команда
# ============================================

@router.message(Command("example"))
async def cmd_example(message: Message):
    """Пример простой команды"""
    await message.answer("Это пример команды! Измени меня в handlers/custom.py")


# ============================================
# ПРИМЕР 2: Команда с кнопками
# ============================================

@router.message(Command("menu"))
async def cmd_menu(message: Message):
    """Пример команды с inline кнопками"""
    
    kb = InlineKeyboardBuilder()
    kb.button(text="Кнопка 1", callback_data="btn1")
    kb.button(text="Кнопка 2", callback_data="btn2")
    kb.button(text="Кнопка 3", callback_data="btn3")
    kb.adjust(2)
    
    await message.answer("Выбери кнопку:", reply_markup=kb.as_markup())


@router.callback_query(F.data == "btn1")
async def callback_btn1(callback: CallbackQuery):
    """Обработка нажатия кнопки 1"""
    await callback.message.edit_text("Ты нажал кнопку 1!")
    await callback.answer()


@router.callback_query(F.data == "btn2")
async def callback_btn2(callback: CallbackQuery):
    """Обработка нажатия кнопки 2"""
    await callback.message.edit_text("Ты нажал кнопку 2!")
    await callback.answer()


@router.callback_query(F.data == "btn3")
async def callback_btn3(callback: CallbackQuery):
    """Обработка нажатия кнопки 3"""
    await callback.message.edit_text("Ты нажал кнопку 3!")
    await callback.answer()


# ============================================
# ПРИМЕР 3: Команда с аргументами
# ============================================

@router.message(Command("echo"))
async def cmd_echo(message: Message):
    """Пример команды с аргументами"""
    
    # Получаем текст после команды
    text = message.text.replace("/echo", "").strip()
    
    if text:
        await message.answer(f"Ты написал: {text}")
    else:
        await message.answer("Использование: /echo <текст>")


# ============================================
# ПРИМЕР 4: Обработка текстовых сообщений
# ============================================

@router.message(F.text.lower() == "привет")
async def handle_hello(message: Message):
    """Ответ на приветствие"""
    await message.answer(f"Привет, {message.from_user.first_name}! 👋")


@router.message(F.text.lower() == "пока")
async def handle_bye(message: Message):
    """Ответ на прощание"""
    await message.answer("До встречи! 👋")


# ============================================
# ДОБАВЬ СВОИ КОМАНДЫ НИЖЕ
# ============================================

# @router.message(Command("mycommand"))
# async def my_command(message: Message):
#     """Моя кастомная команда"""
#     await message.answer("Моя команда работает!")
