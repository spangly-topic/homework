# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: FieldNotes
def print_entry(entry):
    if not entry:
        return
    fields = [
        ("ID", str(entry.id)),
        ("Дата", str(entry.date) if hasattr(entry, 'date') else ''),
        ("Локация", str(entry.location.name) if hasattr(entry, 'location') and entry.location else ''),
        ("Категория", ', '.join(str(c.name) for c in (entry.categories if hasattr(entry, 'categories') else getattr(entry, 'category', None)))) if hasattr(entry, 'categories') else '',
        ("Фото", str(list(getattr(entry, 'photos', [])))[-1:][0].name if hasattr(entry, 'photos') and entry.photos else ''),
    ]
    for label, value in fields:
        print(f"{label:<8}: {value}")
    print("Описание:", entry.description if hasattr(entry, 'description') else '')
