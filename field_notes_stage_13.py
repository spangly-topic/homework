# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: FieldNotes
def search_notes(query: str) -> list[dict]:
    query = query.lower().strip()
    if not query:
        return []
    
    results = []
    for note in notes_db.values():
        searchable_text = (note['text'] + ' ' + 
                           (' '.join(note.get('tags', []))) + ' ' + 
                           note.get('location_name', '')).lower()
        
        if query in searchable_text:
            results.append(note)
    
    return sorted(results, key=lambda x: x['created_at'], reverse=True)
