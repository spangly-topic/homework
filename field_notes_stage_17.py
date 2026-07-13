# === Stage 17: Добавь группировку записей по категориям ===
# Project: FieldNotes
def get_records_by_category(records, category):
    """Возвращает список записей, относящихся к указанной категории."""
    return [r for r in records if r.get('category') == category]
