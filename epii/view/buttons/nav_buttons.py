from epii.controller.controller import Controller, Direction
from epii.view.buttons.base_buttons import BaseButton


class ChangeNoteButton(BaseButton):
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
        self.clicked.connect(self._change_note)

    def change_note(self, direction: Direction) -> None:
        self.controller.change_note(direction)


class LeftNoteButton(ChangeNoteButton):
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setText("Left")

    def _change_note(self) -> None:
        self.change_note(Direction.LEFT)


class RightNoteButton(ChangeNoteButton):
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setText("Right")

    def _change_note(self) -> None:
        self.change_note(Direction.RIGHT)
