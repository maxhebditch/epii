from PySide6.QtCore import QObject, Signal

from epii.model.model import Model
from epii.view_model.direction import Direction


class ViewModel(QObject):
    data_changed = Signal()

    def __init__(self, model: Model) -> None:
        super().__init__()
        self._model = model

    def get_current_note(self) -> str:
        note = self._model.get_active_item()
        return f"{note.content} {note.count}"

    def update_current_note(self) -> None:
        self._model.update_data(self._model.data)
        self.data_changed.emit()

    def update_view(self) -> None:
        self.data_changed.emit()

    def change_current_note(self, direction: Direction) -> None:
        self._model.change_idx(direction.value)
