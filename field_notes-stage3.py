# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: FieldNotes
class FieldNotes:
    def __init__(self):
        self.records = []
        self.locations = {}
        self.categories = {}

    def add_record(self, text, location=None, category=None, photo_path=None):
        record_id = len(self.records) + 1
        record = {
            "id": record_id,
            "text": text,
            "location": location,
            "category": category,
            "photo_path": photo_path or None,
            "timestamp": self._get_timestamp()
        }
        if location:
            self.locations.setdefault(location, []).append(record)
        if category:
            self.categories.setdefault(category, []).append(record)
        self.records.append(record)
        return record

    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().isoformat()
