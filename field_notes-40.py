# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: FieldNotes
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="FieldNotes CLI")
    sub = parser.add_subparsers(dest="command", help="Команда")

    p_add = sub.add_parser("add", help="Добавить наблюдение")
    p_add.add_argument("--location", "-l", help="Локация")
    p_add.add_argument("--category", "-c", help="Категория")
    p_add.add_argument("--photo", help="Путь к фото")
    p_add.add_argument("--note", help="Текст заметки")

    p_search = sub.add_parser("search", help="Поиск наблюдений")
    p_search.add_argument("--q", help="Запрос поиска")

    p_list = sub.add_parser("list", help="Список наблюдений")
    p_list.add_argument("--recent", help="Только последние N")

    return parser.parse_args()
