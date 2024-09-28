from epii.controller.controller import Controller
from epii.view.buttons.base_buttons import BaseButton


class UpdateButton(BaseButton):
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setText("Increment")
        self.clicked.connect(self._update_data)

    def _update_data(self) -> None:
        self.controller.update_data()
