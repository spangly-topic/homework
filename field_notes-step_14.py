# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: FieldNotes
def generate_summary():
    stats = {
        "locations": len(locations),
        "categories": len(categories),
        "notes": len(notes),
        "photos": sum(1 for n in notes if n.get("photo")),
        "recent_note": None,
        "location_names": [loc["name"] for loc in locations],
    }
    if notes:
        stats["recent_note"] = notes[-1]["text"][:80] + "..."
    return f"Сводка: {stats['locations']} локаций, {stats['categories']} категорий, {stats['notes']} заметок ({stats['photos']} с фото). Последняя запись: \"{stats['recent_note']}\""
