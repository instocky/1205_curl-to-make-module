import json
import pyperclip
from pathlib import Path

class Tools:
    @staticmethod
    def save_to_json(data: dict, filename: str = "result.json") -> None:
        """Сохранение результата в JSON файл"""
        try:
            Path(filename).parent.mkdir(parents=True, exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\n✅ Результат сохранен в файл: {filename}")
        except Exception as e:
            print(f"❌ Ошибка при сохранении файла: {e}")

    @staticmethod
    def copy_to_clipboard(data: dict) -> None:
        """Копирование результата в буфер обмена"""
        try:
            json_str = json.dumps(data, indent=2, ensure_ascii=False)
            pyperclip.copy(json_str)
            print("✅ JSON скопирован в буфер обмена")
        except Exception as e:
            print(f"❌ Ошибка при копировании в буфер обмена: {e}")

    @staticmethod
    def process_result(data: dict) -> None:
        """Комплексная обработка результата"""
        # Сохраняем в файл
        Tools.save_to_json(data)
        
        # Копируем в буфер обмена
        Tools.copy_to_clipboard(data)
        
        print("\n👋 Работа завершена")
        exit(0)
