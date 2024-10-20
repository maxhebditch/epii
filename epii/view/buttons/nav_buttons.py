from abc import abstractmethod

from epii.controller.controller import Direction
from epii.view.buttons.base_buttons import BaseButton
from epii.view_model.view_model import ViewModel


class ChangeNoteButton(BaseButton):
    def __init__(self, viewmodel: ViewModel) -> None:
        super().__init__(viewmodel)
        self.clicked.connect(self._change_note)

    @abstractmethod
    def _change_note(self) -> None:  # pragma: no cover
        pass


class LeftNoteButton(ChangeNoteButton):
    def __init__(self, viewmodel: ViewModel) -> None:
        super().__init__(viewmodel)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setText("Left")

    def _change_note(self) -> None:
        self.viewmodel.change_idx(Direction.LEFT)
        self.viewmodel.update_view()


class RightNoteButton(ChangeNoteButton):
    def __init__(self, viewmodel: ViewModel) -> None:
        super().__init__(viewmodel)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setText("Right")

    def _change_note(self) -> None:
        self.viewmodel.change_idx(Direction.RIGHT)
        self.viewmodel.update_view()
