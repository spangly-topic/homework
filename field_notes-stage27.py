# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: FieldNotes
def reset_demo_data():
    """Сбросить все демо-данные: локации, категории, фото-заметки."""
    global _locations, _categories, _photo_notes
    _locations = [
        {"id": 1, "name": "У реки", "coords": (53.7998, 26.7052)},
        {"id": 2, "name": "Лесная поляна", "coords": (53.8143, 26.7135)},
    ]
    _categories = [
        {"id": 1, "name": "Фауна"},
        {"id": 2, "name": "Флора"},
    ]
    _photo_notes = []

def clear_all():
    """Очистить все данные: локации, категории, фото-заметки."""
    global _locations, _categories, _photo_notes
    _locations.clear()
    _categories.clear()
    _photo_notes.clear()
