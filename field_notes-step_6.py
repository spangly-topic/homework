# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: FieldNotes
def filter_records(records, filters=None):
    if not filters: return records
    status = filters.get('status')
    category = filters.get('category')
    tags = set(filters.get('tags', []))
    result = [r for r in records]
    if status is not None: result = [r for r in result if r['status'] == status]
    if category is not None: result = [r for r in result if r.get('category') == category]
    if tags: result = [r for r in result if set(r.get('tags', [])).issuperset(tags)]
    return result
