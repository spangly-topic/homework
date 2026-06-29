# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: FieldNotes
import json, os, sys
from pathlib import Path

INIT_DATA = '''
{
  "locations": [
    {"id": 1, "name": "Лесной массив", "lat": 55.75, "lon": 37.62},
    {"id": 2, "name": "Парк Горького", "lat": 55.78, "lon": 37.60}
  ],
  "categories": [
    {"id": 1, "title": "Растения"},
    {"id": 2, "title": "Животные"}
  ]
}'''

def load_initial_data():
    try:
        data = json.loads(INIT_DATA)
        locations_map = {loc["id"]: loc for loc in data.get("locations", [])}
        categories_map = {cat["id"]: cat for cat in data.get("categories", [])}
        
        if not os.path.exists("data.json"):
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            
            return locations_map, categories_map
        
    except json.JSONDecodeError:
        print("Ошибка при загрузке начальных данных из JSON.")
        sys.exit(1)

if __name__ == "__main__":
    locs, cats = load_initial_data()
    print(f"Загружено {len(locs)} локаций и {len(cats)} категорий.")
