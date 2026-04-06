# Telegram Bot Constructor

<div align="center">

**Universal constructor for creating Telegram bots | Универсальный конструктор для создания Telegram ботов**

Create your bot in 5 minutes | Создай своего бота за 5 минут

[English](#english) | [Русский](#russian)

</div>

---

<a name="english"></a>

## English

### Features

- Modular architecture
- Simple configuration via config
- Ready-made command templates
- Inline and Reply keyboards
- Database support (JSON/SQLite)
- Plugin system
- FSM (Finite State Machine)
- Logging
- Middleware support
- Detailed documentation

### Quick Start

#### 1. Installation

```bash
# Clone repository
git clone https://github.com/yourusername/bot_constructor.git
cd bot_constructor

# Install dependencies
pip install -r requirements.txt
```

#### 2. Setup

```bash
# Copy .env example
copy .env.example .env

# Add your token to .env
BOT_TOKEN=your_bot_token_here
```

#### 3. Configuration

Open `config.py` and customize:

```python
# Bot name
BOT_NAME = "My Awesome Bot"

# Commands
COMMANDS = {
    "start": "Start bot",
    "help": "Help",
}
```

#### 4. Run

```bash
python main.py
```

Done! Bot is running

### Project Structure

```
bot_constructor/
├── main.py                 # Entry point
├── config.py               # Bot settings
├── requirements.txt        # Dependencies
├── .env.example            # Environment variables example
│
├── handlers/               # Command handlers
│   ├── start.py           # /start
│   ├── help_handler.py    # /help
│   ├── about.py           # /about
│   └── custom.py          # Your commands
│
├── keyboards/              # Keyboards
│   ├── inline.py          # Inline buttons
│   └── reply.py           # Reply buttons
│
├── database/               # Database
│   └── db.py              # DB operations
│
├── utils/                  # Utilities
│   └── helpers.py         # Helper functions
│
└── plugins/                # Plugins
    └── __init__.py
```

### How to Use

#### Add Your Command

Open `handlers/custom.py`:

```python
@router.message(Command("mycommand"))
async def my_command(message: Message):
    await message.answer("My command works!")
```

#### Add Buttons

```python
from keyboards.inline import custom_keyboard

buttons = [
    {"text": "Button 1", "callback_data": "btn1"},
    {"text": "Button 2", "callback_data": "btn2"},
]

await message.answer("Choose:", reply_markup=custom_keyboard(buttons))
```

#### Work with Database

```python
from database.db import db

# Save user
db.save_user(user_id, username, first_name)

# Get user
user = db.get_user(user_id)

# Save data
db.set_user_data(user_id, "score", 100)
```

### Examples

#### Simple Bot

```python
# config.py
BOT_NAME = "Hello Bot"
COMMANDS = {"start": "Start", "help": "Help"}
```

#### Bot with Menu

```python
# handlers/custom.py
@router.message(Command("menu"))
async def show_menu(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Option 1", callback_data="opt1")
    kb.button(text="Option 2", callback_data="opt2")
    kb.adjust(2)
    await message.answer("Menu:", reply_markup=kb.as_markup())
```

### Configuration

```python
# Basic
BOT_NAME = "My Bot"
BOT_DESCRIPTION = "Description"
VERSION = "1.0.0"

# Database
DATABASE_TYPE = "json"  # or "sqlite"
DATABASE_PATH = "data/database.json"

# Logging
LOG_LEVEL = "INFO"
LOG_TO_FILE = True

# Admins
ADMINS = [123456789]
```

### License

MIT License - use as you wish!

### Support

- Telegram: [@YourUsername](https://t.me/YourUsername)
- Issues: [GitHub Issues](https://github.com/yourusername/bot_constructor/issues)

---

<a name="russian"></a>

## Русский

### Возможности

- Модульная архитектура
- Простая настройка через config
- Готовые шаблоны команд
- Inline и Reply клавиатуры
- База данных (JSON/SQLite)
- Система плагинов
- FSM (машина состояний)
- Логирование
- Middleware поддержка
- Подробная документация

### Быстрый старт

#### 1. Установка

```bash
# Клонируй репозиторий
git clone https://github.com/yourusername/bot_constructor.git
cd bot_constructor

# Установи зависимости
pip install -r requirements.txt
```

#### 2. Настройка

```bash
# Скопируй пример .env
copy .env.example .env

# Добавь свой токен в .env
BOT_TOKEN=your_bot_token_here
```

#### 3. Конфигурация

Открой `config.py` и настрой под себя:

```python
# Название бота
BOT_NAME = "Мой Крутой Бот"

# Команды
COMMANDS = {
    "start": "Начать работу",
    "help": "Помощь",
}
```

#### 4. Запуск

```bash
python main.py
```

Готово! Бот запущен

### Структура проекта

```
bot_constructor/
├── main.py                 # Точка входа
├── config.py               # Настройки бота
├── requirements.txt        # Зависимости
├── .env.example            # Пример переменных окружения
│
├── handlers/               # Обработчики команд
│   ├── start.py           # /start
│   ├── help_handler.py    # /help
│   ├── about.py           # /about
│   └── custom.py          # Твои команды
│
├── keyboards/              # Клавиатуры
│   ├── inline.py          # Inline кнопки
│   └── reply.py           # Reply кнопки
│
├── database/               # База данных
│   └── db.py              # Работа с БД
│
├── utils/                  # Утилиты
│   └── helpers.py         # Вспомогательные функции
│
└── plugins/                # Плагины
    └── __init__.py
```

### Как использовать

#### Добавить свою команду

Открой `handlers/custom.py`:

```python
@router.message(Command("mycommand"))
async def my_command(message: Message):
    await message.answer("Моя команда работает!")
```

#### Добавить кнопки

```python
from keyboards.inline import custom_keyboard

buttons = [
    {"text": "Кнопка 1", "callback_data": "btn1"},
    {"text": "Кнопка 2", "callback_data": "btn2"},
]

await message.answer("Выбери:", reply_markup=custom_keyboard(buttons))
```

#### Работа с базой данных

```python
from database.db import db

# Сохранить пользователя
db.save_user(user_id, username, first_name)

# Получить пользователя
user = db.get_user(user_id)

# Сохранить данные
db.set_user_data(user_id, "score", 100)
```

### Примеры

#### Простой бот

```python
# config.py
BOT_NAME = "Hello Bot"
COMMANDS = {"start": "Начать", "help": "Помощь"}
```

#### Бот с меню

```python
# handlers/custom.py
@router.message(Command("menu"))
async def show_menu(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Опция 1", callback_data="opt1")
    kb.button(text="Опция 2", callback_data="opt2")
    kb.adjust(2)
    await message.answer("Меню:", reply_markup=kb.as_markup())
```

### Настройки

```python
# Основные
BOT_NAME = "Мой Бот"
BOT_DESCRIPTION = "Описание"
VERSION = "1.0.0"

# База данных
DATABASE_TYPE = "json"  # или "sqlite"
DATABASE_PATH = "data/database.json"

# Логирование
LOG_LEVEL = "INFO"
LOG_TO_FILE = True

# Админы
ADMINS = [123456789]
```

### Лицензия

MIT License - используй как хочешь!

### Поддержка

- Telegram: [Ghost](https://t.me/LittleWhiteGhost)
- Issues: [GitHub Issues](https://github.com/LittleWhiteGhost/tg-bot-constructor/issues)

---

<div align="center">

**Made with love for the community | Сделано с любовью для сообщества**

Star if you like the project | Поставь звезду если проект понравился

</div>
