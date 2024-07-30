from enum import Enum

from epii.view_model.view_model import ViewModel


class Direction(Enum):
    LEFT = -1
    RIGHT = 1


class Controller:
    def __init__(self, viewmodel: ViewModel) -> None:
        self.viewmodel = viewmodel

    def update_data(self) -> None:
        self.viewmodel.update_data()

    def change_note(self, direction: Direction) -> None:
        print(f"change_note {direction}")
