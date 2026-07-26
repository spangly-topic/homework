# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: FieldNotes
def parse_date(s):
    """Parse a date string in formats: YYYY-MM-DD, DD.MM.YYYY, MM.DD.YYYY."""
    import re
    s = s.strip()
    if not s:
        return None
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%m.%d.%Y'):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise ValueError(f"Не удалось распознать дату: '{s}'. Используйте формат YYYY-MM-DD или DD.MM.YYYY.")
