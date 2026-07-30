# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: FieldNotes
def print_metrics():
    metrics = {
        "locations": len(LOCATIONS),
        "categories": len(CATEGORIES),
        "notes": len(NOTES),
        "photos": sum(len(n["photos"]) for n in NOTES),
        "searches": SEARCHES,
    }
    print("=== FieldNotes Metrics ===")
    for k, v in metrics.items():
        print(f"  {k}: {v}")

print_metrics()
