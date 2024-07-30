from PySide6.QtWidgets import QPushButton

from epii.controller.controller import Controller


class BaseButton(QPushButton):
    def __init__(self, controller: Controller) -> None:
        super().__init__()
        self.controller = controller
