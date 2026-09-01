# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: FieldNotes
import pytest
from datetime import datetime, timedelta

def test_add_note_invalid_date():
    notes = []
    categories = []
    locations = []
    photos = []
    try:
        notes.append({
            "date": "2024-13-01",
            "category": "test",
            "location": "test",
            "photo": "test.jpg",
            "text": "test"
        })
    except Exception:
        pass
    assert len(notes) == 0

def test_add_note_to_nonexistent_category():
    notes = []
    categories = []
    locations = []
    photos = []
    categories.append({"name": "valid"})
    notes.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": "nonexistent",
        "location": "test",
        "photo": "test.jpg",
        "text": "test"
    })
    assert len(notes) == 0

def test_search_in_empty_notes():
    notes = []
    categories = []
    locations = []
    photos = []
    results = search_notes(notes, "")
    assert len(results) == 0

def test_search_with_no_match():
    notes = [{"date": "2024-01-01", "category": "bird", "location": "forest", "photo": "b1.jpg", "text": "sparrow"}]
    categories = []
    locations = []
    photos = []
    results = search_notes(notes, "elephant")
    assert len(results) == 0

def test_add_photo_without_note():
    notes = []
    categories = []
    locations = []
    photos = []
    photos.append({"note_id": 999, "filename": "orphan.jpg", "path": "photos/orphan.jpg"})
    assert len(photos) == 1
