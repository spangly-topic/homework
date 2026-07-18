# === Stage 20: Добавь восстановление записей из архива ===
# Project: FieldNotes
def restore_from_archive(archive_path):
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines()]
    except FileNotFoundError:
        print(f"Архив не найден: {archive_path}")
        return 0

    count = 0
    for line in lines:
        if not line or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) < 5:
            print(f"Плохая строка в архиве: {line}")
            continue

        date_str, time_str, location, category, note = parts[:5]

        try:
            obs_date = datetime.strptime(date_str.strip(), '%Y-%m-%d')
        except ValueError:
            print(f"Неверная дата в строке: {date_str}")
            continue

        try:
            obs_time = datetime.strptime(time_str.strip(), '%H:%M').time() if time_str else None
        except ValueError:
            pass

        photo_path = parts[5].strip() if len(parts) > 5 else ''
        if photo_path and not os.path.isfile(photo_path):
            print(f"Фото не найдено: {photo_path}")
            continue

        obs = Observation(
            date=obs_date,
            time=obs_time,
            location=location.strip(),
            category=category.strip(),
            note=note.strip(),
            photo=photo_path if photo_path else None,
        )
        FieldNotes._observations.append(obs)
        count += 1

    print(f"Восстановлено {count} записей из архива.")
    return count
