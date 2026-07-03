# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: FieldNotes
import json, os

def load_notes_from_file(filepath: str) -> list[dict]:
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'notes' in data:
            print("Файл содержит один объект с полем notes.")
            return data.get('notes', [])
        else:
            raise ValueError("Неверный формат JSON файла.")
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return []

if __name__ == "__main__":
    notes = load_notes_from_file("data.json")
    for note in notes[:2]:
        print(note)
