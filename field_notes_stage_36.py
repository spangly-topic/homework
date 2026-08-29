# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: FieldNotes
def repair_data(storage):
    """Проверяет целостность данных и пытается исправить простые проблемы."""
    try:
        records = storage.get("records", [])
        locations = storage.get("locations", [])
        categories = storage.get("categories", [])
        notes = storage.get("notes", [])
        if not all([records, locations, categories, notes]):
            raise ValueError("Не все данные инициализированы")
    except Exception as e:
        print(f"Ошибка проверки данных: {e}")
        return False

    for note in notes:
        if "photo_path" in note and not note["photo_path"]:
            note["photo_path"] = ""

    for record in records:
        if "location_id" in record and record["location_id"] not in [loc["id"] for loc in locations]:
            record["location_id"] = None

    for record in records:
        if "category_id" in record and record["category_id"] not in [cat["id"] for cat in categories]:
            record["category_id"] = None

    for note in notes:
        if "record_id" in note and note["record_id"] not in [rec["id"] for rec in records]:
            note["record_id"] = None

    storage["records"] = records
    storage["locations"] = locations
    storage["categories"] = categories
    storage["notes"] = notes
    print("Данные проверены и, при необходимости, исправлены")
    return True
