# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: FieldNotes
def edit_note(note_id: int, **kwargs) -> dict | None:
    if note_id not in notes_db:
        return {"success": False, "error": "Note not found"}
    
    original = notes_db[note_id].copy()
    for key, value in kwargs.items():
        if hasattr(original.get(key), 'append') and isinstance(value, list):
            original[key].extend(value)
        else:
            original[key] = value
    
    # Удаляем пустые поля (кроме id и timestamp)
    for field in ['location', 'category', 'photos', 'description']:
        if not original.get(field):
            del original[field]
    
    notes_db[note_id] = original
    return {"success": True, "note": original}
