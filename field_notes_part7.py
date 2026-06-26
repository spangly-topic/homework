# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: FieldNotes
def sort_records(records, key='date', reverse=True):
    if key == 'priority':
        priority_map = {'high': 0, 'medium': 1, 'low': 2}
        return sorted(records, key=lambda r: (r.get('priority') in priority_map and priority_map[r['priority']] or 3, r.get('date', ''), r.get('name', '')), reverse=reverse)
    elif key == 'name':
        return sorted(records, key=lambda r: (r.get('date', ''), r.get('name', '')))
    else:
        return sorted(records, key=lambda r: r.get(key, ''), reverse=reverse)
