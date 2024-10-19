from unittest.mock import Mock

from epii.controller.controller import Controller, Direction
from epii.view_model.view_model import ViewModel


def test_update_data():
    controller = Controller(Mock(spec=ViewModel))
    controller.update_data()
    controller.viewmodel.update_data.assert_called_once()


def test_change_idx_right():
    controller = Controller(Mock(spec=ViewModel))
    controller.change_note(Direction.RIGHT)
    controller.viewmodel.change_idx.assert_called_once_with(Direction.RIGHT.value)
    controller.viewmodel.update_view.assert_called_once()


def test_change_idx_left():
    controller = Controller(Mock(spec=ViewModel))
    controller.change_note(Direction.LEFT)
    controller.viewmodel.change_idx.assert_called_once_with(Direction.LEFT.value)
    controller.viewmodel.update_view.assert_called_once()