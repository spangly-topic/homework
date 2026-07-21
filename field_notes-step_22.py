# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: FieldNotes
def check_overdue_reminders():
    now = datetime.datetime.now()
    overdue = []
    for entry in reminders:
        if entry.get("deadline") and isinstance(entry["deadline"], datetime.datetime):
            if entry["deadline"] < now:
                overdue.append((entry, "overdue"))
            elif entry["deadline"].date() == now.date():
                overdue.append((entry, "today"))
    return overdue
