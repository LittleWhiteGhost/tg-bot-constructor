"""
Вспомогательные функции
"""

from datetime import datetime
from typing import List
import config


def format_user_mention(user_id: int, name: str) -> str:
    """Форматирование упоминания пользователя"""
    return f"[{name}](tg://user?id={user_id})"


def is_admin(user_id: int) -> bool:
    """Проверка является ли пользователь админом"""
    return user_id in config.ADMINS


def get_current_time() -> str:
    """Получить текущее время"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def truncate_text(text: str, max_length: int = 100) -> str:
    """Обрезать текст до максимальной длины"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def split_message(text: str, max_length: int = 4096) -> List[str]:
    """Разделить длинное сообщение на части"""
    if len(text) <= max_length:
        return [text]
    
    parts = []
    while text:
        if len(text) <= max_length:
            parts.append(text)
            break
        
        # Ищем последний перенос строки
        split_pos = text.rfind('\n', 0, max_length)
        if split_pos == -1:
            split_pos = max_length
        
        parts.append(text[:split_pos])
        text = text[split_pos:].lstrip()
    
    return parts


def escape_markdown(text: str) -> str:
    """Экранирование специальных символов Markdown"""
    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in special_chars:
        text = text.replace(char, f'\\{char}')
    return text


def format_list(items: List[str], numbered: bool = False) -> str:
    """Форматирование списка"""
    if numbered:
        return "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])
    return "\n".join([f"• {item}" for item in items])


def validate_user_input(text: str, min_length: int = 1, max_length: int = 1000) -> bool:
    """Валидация пользовательского ввода"""
    if not text or not text.strip():
        return False
    
    text_length = len(text.strip())
    return min_length <= text_length <= max_length
