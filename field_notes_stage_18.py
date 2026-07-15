# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: FieldNotes
class Tag:
    def __init__(self, name, color=None):
        self.name = name.lower().strip()
        if not self.name:
            raise ValueError("Tag name cannot be empty")
        self.color = color or random.choice(
            ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]
        )

    def __eq__(self, other):
        if isinstance(other, Tag): return self.name == other.name
        return False

    def __hash__(self): return hash(self.name)

    def __repr__(self): return f"<Tag {self.name!r}>"


class TagOperation:
    """Compact add/remove tag logic with auto-tagging."""
    @staticmethod
    def add_tag(note, name):
        if isinstance(name, str):
            tag = Tag(name)
        else:
            tag = name
        note.tags.add(tag)
        return tag

    @staticmethod
    def remove_tag(note, name):
        if isinstance(name, str):
            target = Tag(name)
        else:
            target = name
        removed = False
        for t in list(note.tags):
            if t == target:
                note.tags.remove(t)
                removed = True
                break
        return removed

    @staticmethod
    def auto_tag_by_date(note, tag_name):
        """Auto-tag notes by year/month/day matching."""
        try:
            ts = datetime.fromisoformat(note.timestamp or "1970-01-01")
        except Exception:
            return False
        parts = tag_name.replace(" ", "-").split("-")
        if len(parts) not in (2, 3): return False
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2]) if len(parts) == 3 else None
        if ts.year != year: return False
        if month and ts.month != month: return False
        if day and ts.day != day: return False
        try:
            Tag(tag_name)
            note.tags.add(Tag(tag_name))
            return True
        except ValueError:
            return False
