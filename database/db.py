"""
Работа с базой данных
"""

import json
import os
from typing import Any, Dict, Optional

import config


class Database:
    """Класс для работы с базой данных"""
    
    def __init__(self):
        self.db_type = config.DATABASE_TYPE
        self.db_path = config.DATABASE_PATH
        
        # Создание директории если не существует
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        # Инициализация БД
        if self.db_type == "json":
            self._init_json()
    
    def _init_json(self):
        """Инициализация JSON базы"""
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump({"users": {}, "data": {}}, f, ensure_ascii=False, indent=2)
    
    def _load_json(self) -> Dict:
        """Загрузка JSON базы"""
        with open(self.db_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _save_json(self, data: Dict):
        """Сохранение JSON базы"""
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    # ============================================
    # РАБОТА С ПОЛЬЗОВАТЕЛЯМИ
    # ============================================
    
    def save_user(self, user_id: int, username: str = None, first_name: str = None):
        """Сохранить пользователя"""
        data = self._load_json()
        
        user_id_str = str(user_id)
        if user_id_str not in data["users"]:
            data["users"][user_id_str] = {
                "user_id": user_id,
                "username": username,
                "first_name": first_name,
                "registered_at": None
            }
        
        self._save_json(data)
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Получить пользователя"""
        data = self._load_json()
        return data["users"].get(str(user_id))
    
    def get_all_users(self) -> Dict:
        """Получить всех пользователей"""
        data = self._load_json()
        return data["users"]
    
    def delete_user(self, user_id: int):
        """Удалить пользователя"""
        data = self._load_json()
        user_id_str = str(user_id)
        if user_id_str in data["users"]:
            del data["users"][user_id_str]
            self._save_json(data)
    
    # ============================================
    # РАБОТА С ДАННЫМИ
    # ============================================
    
    def set_data(self, key: str, value: Any):
        """Сохранить данные"""
        data = self._load_json()
        data["data"][key] = value
        self._save_json(data)
    
    def get_data(self, key: str, default: Any = None) -> Any:
        """Получить данные"""
        data = self._load_json()
        return data["data"].get(key, default)
    
    def delete_data(self, key: str):
        """Удалить данные"""
        data = self._load_json()
        if key in data["data"]:
            del data["data"][key]
            self._save_json(data)
    
    # ============================================
    # РАБОТА С ПОЛЬЗОВАТЕЛЬСКИМИ ДАННЫМИ
    # ============================================
    
    def set_user_data(self, user_id: int, key: str, value: Any):
        """Сохранить данные пользователя"""
        data = self._load_json()
        user_id_str = str(user_id)
        
        if user_id_str not in data["users"]:
            self.save_user(user_id)
            data = self._load_json()
        
        if "data" not in data["users"][user_id_str]:
            data["users"][user_id_str]["data"] = {}
        
        data["users"][user_id_str]["data"][key] = value
        self._save_json(data)
    
    def get_user_data(self, user_id: int, key: str, default: Any = None) -> Any:
        """Получить данные пользователя"""
        data = self._load_json()
        user_id_str = str(user_id)
        
        if user_id_str in data["users"] and "data" in data["users"][user_id_str]:
            return data["users"][user_id_str]["data"].get(key, default)
        
        return default


# Создание глобального экземпляра
db = Database()
