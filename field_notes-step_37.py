# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: FieldNotes
import unittest

class TestFieldNotes(unittest.TestCase):
    def test_add_location(self):
        from fieldnotes import FieldNotes
        fn = FieldNotes()
        loc = fn.add_location("Park", "city", "nature")
        self.assertIn(loc, fn.locations)
        self.assertEqual(loc.name, "Park")
        self.assertEqual(loc.city, "city")
        self.assertEqual(loc.category, "nature")

    def test_add_photo_note(self):
        from fieldnotes import FieldNotes
        fn = FieldNotes()
        fn.add_location("Forest", "Moscow", "nature")
        note = fn.add_photo_note("Forest", "Sunset.jpg", "Beautiful sunset", "2024-01-01")
        self.assertIn(note, fn.notes)
        self.assertEqual(note.location, "Forest")
        self.assertEqual(note.image, "Sunset.jpg")
        self.assertEqual(note.text, "Beautiful sunset")
        self.assertEqual(note.date, "2024-01-01")

    def test_search_notes(self):
        from fieldnotes import FieldNotes
        fn = FieldNotes()
        fn.add_location("Beach", "Sochi", "nature")
        fn.add_photo_note("Beach", "Sand.jpg", "Soft sand", "2024-02-01")
        fn.add_photo_note("Forest", "Tree.jpg", "Old tree", "2024-02-02")
        results = fn.search_notes("Beach")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].image, "Sand.jpg")

    def test_search_locations(self):
        from fieldnotes import FieldNotes
        fn = FieldNotes()
        fn.add_location("Lake", "Novosibirsk", "nature")
        fn.add_location("Mountain", "Krasnoyarsk", "nature")
        results = fn.search_locations("nature")
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()
