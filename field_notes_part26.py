# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: FieldNotes
def demo():
    print("=== FieldNotes Demo ===")
    for loc in LOCATIONS:
        print(f"\n[{loc.name}] {loc.description}")
        for note in loc.notes:
            print(f"  - [{note.category}] {note.title} ({note.date})")
            if note.photo:
                print(f"    фото: {note.photo.url}")
    print("\n=== Поиск ===")
    q = input("Введите запрос (или Enter для выхода): ")
    while q.strip():
        results = search(q)
        for r in results[:5]:
            print(f"\n>> {r.note.title} ({r.loc.name}) — {r.note.date}")
        q = input("\nСледующий запрос: ").strip()
