# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: FieldNotes
import json, os
from datetime import datetime
from typing import Optional

class FieldNote:
    def __init__(self, id: str, location: str, category: str, content: str, photo_url: Optional[str] = None):
        self.id = id
        self.location = location
        self.category = category
        self.content = content
        self.photo_url = photo_url
        self.created_at = datetime.now().isoformat()

class FieldNotesApp:
    def __init__(self, data_file="fieldnotes.json"):
        self.data_file = data_file
        self.notes: list[FieldNote] = []
        self.categories: set[str] = set()
        self.locations: set[str] = set()
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for note_data in data.get('notes', []):
                    self.notes.append(FieldNote(**note_data))
                self.categories.update(note['category'] for note in self.notes)
                self.locations.update(note['location'] for note in self.notes)

    def add_note(self, location: str, category: str, content: str, photo_url: Optional[str] = None) -> FieldNote:
        note = FieldNote(id=str(len(self.notes)+1), location=location, category=category, content=content, photo_url=photo_url)
        self.notes.append(note)
        self.categories.add(category)
        self.locations.add(location)
        self._save()
        return note

    def _save(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({'notes': [n.__dict__ for n in self.notes], 'categories': list(self.categories), 'locations': list(self.locations)}, f, ensure_ascii=False)

    def search(self, query: str):
        return [n for n in self.notes if query.lower() in n.content.lower() or query.lower() in n.location.lower()]

app = FieldNotesApp()
