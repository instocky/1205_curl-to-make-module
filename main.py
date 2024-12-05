import argparse
import sys
from curl_converter import CurlToMakeConverter
from tools import Tools

class CurlConverterCLI:
    def __init__(self):
        self.converter = CurlToMakeConverter()

    def process_single_curl(self, curl_command: str) -> None:
        """Обработка одного curl запроса"""
        try:
            result = self.converter.parse_curl(curl_command)
            Tools.process_result(result)
        except Exception as e:
            print(f"❌ Ошибка при обработке curl команды: {e}")
            sys.exit(1)
            
    def interactive_mode(self) -> None:
        """Интерактивный режим работы с поддержкой многострочного ввода"""
        print("=== Конвертер CURL в Make.com HTTP модуль ===")
        print("Введите curl запрос (для завершения ввода нажмите Enter дважды):")
        
        try:
            lines = []
            while True:
                line = input()
                if not line and lines:  # Если строка пустая и уже есть введенные строки
                    break
                if line:
                    lines.append(line)
            
            if lines:
                # Объединяем строки, удаляя символы переноса
                curl_command = ' '.join(line.rstrip('\\').strip() for line in lines)
                self.process_single_curl(curl_command)
            else:
                print("❌ Пустой ввод")
                sys.exit(1)
            
        except KeyboardInterrupt:
            print("\n👋 Программа завершена пользователем")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            sys.exit(1)

    def read_curl_from_file(self, filename: str) -> str:
        """Чтение curl команды из файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Объединяем строки, удаляя символы переноса
                return ' '.join(line.rstrip('\\').strip() for line in lines if line.strip())
        except Exception as e:
            print(f"❌ Ошибка чтения файла: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Конвертер CURL запросов в Make.com HTTP модуль')
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument('--curl', type=str, help='CURL запрос для обработки')
    group.add_argument('--file', type=str, help='Путь к файлу с CURL запросом')
    
    args = parser.parse_args()
    converter_cli = CurlConverterCLI()

    try:
        if args.curl:
            converter_cli.process_single_curl(args.curl)
        elif args.file:
            curl = converter_cli.read_curl_from_file(args.file)
            converter_cli.process_single_curl(curl)
        else:
            converter_cli.interactive_mode()
    except KeyboardInterrupt:
        print("\n👋 Программа завершена пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()