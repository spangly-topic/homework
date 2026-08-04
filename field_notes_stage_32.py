# === Stage 32: Добавь журнал действий пользователя ===
# Project: FieldNotes
class ActionLog:
    def __init__(self):
        self._entries = []

    def add(self, user, action_type, description, timestamp=None):
        if timestamp is None:
            import datetime as _dt; timestamp = _dt.datetime.now()
        entry = {
            "user": user,
            "type": action_type,
            "description": description,
            "timestamp": timestamp.isoformat(),
        }
        self._entries.append(entry)

    def get(self):
        return list(self._entries)

    def recent(self, n=10):
        return list(reversed(self._entries[-n:]))

log = ActionLog()
