# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: FieldNotes
def archive_notes(limit=10, oldest_first=True):
    if not notes:
        print("Нет записей для архивации.")
        return
    sorted_notes = sorted(notes, key=lambda n: n["date"], reverse=not oldest_first)
    to_archive = sorted_notes[:limit]
    for note in to_archive:
        note["archived"] = True
    print(f"Архивировано {len(to_archive)} записей.")
