# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: FieldNotes
def export_to_json():
    data = {
        "locations": locations,
        "categories": categories,
        "notes": notes,
        "photos": photos,
        "search_index": search_index
    }
    return json.dumps(data, indent=2)
