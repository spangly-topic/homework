# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: FieldNotes
def delete_entry(entry_id):
    try:
        entries = load_entries()
        if entry_id in entries:
            del entries[entry_id]
            save_entries(entries)
            print(f"Запись #{entry_id} удалена.")
        else:
            print("ID записи не найден.")
    except FileNotFoundError:
        print("Файл записей не существует.")
