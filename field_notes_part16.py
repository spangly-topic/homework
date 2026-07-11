# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: FieldNotes
def monthly_stats(fieldnotes):
    from collections import defaultdict
    stats = defaultdict(lambda: {"total": 0, "entries": {}})
    for fn in fieldnotes.values():
        if not hasattr(fn, 'date') or not fn.date: continue
        key = fn.date.strftime('%Y-%m')
        stats[key]["total"] += 1
        stats[key]["entries"][fn.id] = fn.title
    return dict(sorted(stats.items()))

def print_monthly_stats(fieldnotes):
    result = monthly_stats(fieldnotes)
    if not result:
        print("Сезонные данные отсутствуют.")
    else:
        print(f"{'Месяц':<10} {'Всего записей':>12}")
        for month, data in result.items():
            print(f"{month:<10} {data['total']:>12}")

if __name__ == "__main__":
    fieldnotes = {}  # предполагается, что это глобальный словарь полей
    if not hasattr(fieldnotes, 'add'):
        def add(title, location=None, category=None, date=None):
            global fieldnotes
            fn_id = len(fieldnotes) + 1
            entry = {"id": fn_id, "title": title, "location": location, "category": category, "date": date}
            fieldnotes[fn_id] = entry
            return entry
        fieldnotes.add = add
    print_monthly_stats(fieldnotes)
