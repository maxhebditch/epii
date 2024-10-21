from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget

from epii.view.buttons.nav_buttons import LeftNoteButton, RightNoteButton
from epii.view.buttons.update_buttons import UpdateButton
from epii.view_model.view_model import ViewModel

min_width = 250
min_height = 200


class Header(QLabel):
    def __init__(self, viewmodel: ViewModel) -> None:
        super().__init__()
        self.viewmodel = viewmodel
        self._init_ui()
        self.viewmodel.data_changed.connect(self._update_text)

    def _init_ui(self) -> None:
        self.setText(self.viewmodel.get_notes_all())

    def _update_text(self) -> None:
        self.setText(self.viewmodel.get_notes_all())


class View(QMainWindow):
    def __init__(self, viewmodel: ViewModel) -> None:
        super().__init__()
        self.viewmodel = viewmodel
        self._init_ui()

    def _init_ui(self) -> None:
        self._init_window_properties()
        self._init_content()

    def _init_window_properties(self) -> None:
        self.setMinimumSize(min_width, min_height)
        self.setWindowTitle("epii")

    def _init_content(self) -> None:
        layout = QVBoxLayout()
        layout.addWidget(Header(self.viewmodel))
        layout.addWidget(UpdateButton(self.viewmodel))
        layout.addWidget(LeftNoteButton(self.viewmodel))
        layout.addWidget(RightNoteButton(self.viewmodel))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
