from epii.view.buttons.base_buttons import BaseButton
from epii.view_model.view_model import ViewModel


class UpdateButton(BaseButton):
    def __init__(self, viewmodel: ViewModel) -> None:
        super().__init__(viewmodel)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setText("Increment")
        self.clicked.connect(self._update_current_note)

    def _update_current_note(self) -> None:
        self.viewmodel.update_current_note()
