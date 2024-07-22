from PySide6.QtCore import QObject, Signal

from epii.model.model import Model


class ViewModel(QObject):
    data_changed = Signal()

    def __init__(self, model: Model) -> None:
        super().__init__()
        self._model = model

    def get_data(self) -> str:
        return self._model.get_data()

    def update_data(self) -> None:
        self._model.update_data(self._model.data)
        self.data_changed.emit()
