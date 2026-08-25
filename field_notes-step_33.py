# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: FieldNotes
import bisect
from typing import Optional

class UndoStack:
    def __init__(self, max_depth: int = 10):
        self._history: list = []
        self._max_depth = max_depth

    def save(self, state: dict) -> None:
        self._history.append(dict(state))
        if len(self._history) > self._max_depth:
            self._history.pop(0)

    def undo(self) -> Optional[dict]:
        if not self._history:
            return None
        return self._history.pop()

    def redo(self) -> Optional[dict]:
        return self._history.pop() if self._history else None
