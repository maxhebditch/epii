from PySide6.QtWidgets import QPushButton

from epii.view_model.view_model import ViewModel


class BaseButton(QPushButton):
    def __init__(self, viewmodel: ViewModel) -> None:
        super().__init__()
        self.viewmodel = viewmodel
