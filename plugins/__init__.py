"""
Система плагинов - добавь свои плагины здесь!
"""

# Пример структуры плагина:
#
# class MyPlugin:
#     def __init__(self, bot, dp):
#         self.bot = bot
#         self.dp = dp
#     
#     async def setup(self):
#         """Инициализация плагина"""
#         pass
#     
#     async def handle_command(self, message):
#         """Обработка команды"""
#         pass

# Список доступных плагинов
AVAILABLE_PLUGINS = {}

# Функция для регистрации плагина
def register_plugin(name, plugin_class):
    """Регистрация плагина"""
    AVAILABLE_PLUGINS[name] = plugin_class
