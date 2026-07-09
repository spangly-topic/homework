# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: FieldNotes
def weekly_stats(records):
    """Return dict of ISO-week -> list of record summaries."""
    from datetime import datetime, timedelta
    stats = {}
    for r in records:
        if not hasattr(r, 'timestamp') or r.timestamp is None:
            continue
        dt = r.timestamp
        # Find Monday of the week containing this date
        monday = (dt - timedelta(days=dt.weekday())).date()
        key = monday.isoformat()
        stats.setdefault(key, []).append({
            'summary': str(r),
            'location': getattr(r, 'location', None),
            'category': getattr(r, 'category', None),
        })
    return dict(sorted(stats.items()))
