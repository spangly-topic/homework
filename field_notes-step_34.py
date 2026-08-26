# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: FieldNotes
class Template:
    def __init__(self, name, location=None, category=None, note=""):
        self.name = name
        self.location = location
        self.category = category
        self.note = note

    def apply(self, entry):
        if self.location:
            entry.location = self.location
        if self.category:
            entry.category = self.category
        if self.note:
            entry.note = self.note
        return entry

def get_templates():
    return [
        Template("Птица", category="птицы", note="Наблюдение птицы: вид, количество, поведение"),
        Template("Растение", category="растения", note="Описание растения: высота, цвет, листья"),
        Template("Млекопитающее", category="животные", note="Наблюдение млекопитающего: вид, поведение, среда обитания"),
        Template("Общее", category=None, note="Заметка: описание наблюдения"),
    ]
