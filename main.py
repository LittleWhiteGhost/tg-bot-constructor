"""
Главный файл бота - точка входа
"""

import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# Импорт конфига
import config

# Импорт обработчиков
from handlers import start, help_handler, about, custom

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if config.LOG_TO_FILE:
    os.makedirs('logs', exist_ok=True)
    file_handler = logging.FileHandler(config.LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(file_handler)

logger = logging.getLogger(__name__)

# Инициализация бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле!")

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage() if config.FSM_STORAGE == "memory" else MemoryStorage()
dp = Dispatcher(storage=storage)


async def on_startup():
    """Действия при запуске бота"""
    logger.info(f"Бот {config.BOT_NAME} v{config.VERSION} запущен!")
    logger.info(f"Автор: {config.AUTHOR}")
    
    # Создание необходимых директорий
    os.makedirs('data', exist_ok=True)
    
    # Установка команд бота
    from aiogram.types import BotCommand
    commands = [
        BotCommand(command=cmd, description=desc)
        for cmd, desc in config.COMMANDS.items()
    ]
    await bot.set_my_commands(commands)
    logger.info(f"Установлено {len(commands)} команд")


async def on_shutdown():
    """Действия при остановке бота"""
    logger.info("Бот остановлен")
    await bot.session.close()


async def main():
    """Главная функция"""
    
    # Регистрация обработчиков
    dp.include_router(start.router)
    dp.include_router(help_handler.router)
    dp.include_router(about.router)
    dp.include_router(custom.router)
    
    # Регистрация событий
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    # Загрузка плагинов
    if config.ENABLE_PLUGINS:
        logger.info("Загрузка плагинов...")
        # Здесь можно добавить загрузку плагинов
    
    # Запуск бота
    try:
        logger.info("Начинаю polling...")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
