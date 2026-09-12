# === Stage 45: Добавь восстановление из резервной копии ===
# Project: FieldNotes
import json, os

def recover_backup(fieldnotes_db, backup_path):
    if not backup_path or not os.path.isfile(backup_path):
        print("Резервная копия не найдена.")
        return False
    with open(backup_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Неверный формат резервной копии.")
            return False
    if not isinstance(data, dict):
        print("Резервная копия имеет неверную структуру.")
        return False
    if not all(key in data for key in ("locations", "categories", "notes", "settings", "version")):
        print("Резервная копия неполная.")
        return False
    fieldnotes_db.update(data)
    print(f"Восстановлено из {backup_path}.")
    return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Использование: python fieldnotes.py <backup.json>")
        sys.exit(1)
    db = {}
    if recover_backup(db, sys.argv[1]):
        print("Восстановление успешно завершено.")
    else:
        sys.exit(1)
