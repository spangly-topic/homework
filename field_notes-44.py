# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: FieldNotes
def backup_data_file(path: str, backup_dir: str = "backups") -> str:
    """Создает резервную копию файла данных и возвращает путь к копии."""
    import os
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = os.path.basename(path)
    stem, ext = os.path.splitext(base)
    backup_path = os.path.join(backup_dir, f"{stem}_backup_{ts}{ext}")
    with open(path, "rb") as src, open(backup_path, "wb") as dst:
        dst.write(src.read())
    return backup_path
