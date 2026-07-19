# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: FieldNotes
def add_reminder(name, date_str):
    """Добавить напоминание с датой (YYYY-MM-DD)."""
    reminders = []
    try:
        import datetime
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        
        if date_str < today or date_str > (today + datetime.timedelta(days=365)):
            print(f"⚠️ Дата напоминания выходит за допустимый диапазон (сегодня + 1 год).")
            return False
        
        reminders.append({"name": name, "date": target_date})
        
        if reminders:
            reminders.sort(key=lambda r: r["date"])
            
        print(f"✅ Напоминание добавлено: «{name}» на {date_str}")
        return True
    except ValueError as e:
        print(f"❌ Ошибка: некорректная дата. Используйте формат YYYY-MM-DD (например, 2025-12-31).")
        return False

# Пример использования:
if __name__ == "__main__":
    add_reminder("Подготовить отчёт", "2026-01-15")
