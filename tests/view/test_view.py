from unittest.mock import Mock, patch

import pytest
from PySide6.QtCore import Qt
from PySide6.QtTest import QSignalSpy, QTest
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from epii.controller.controller import Controller
from epii.model.model import Model
from epii.notes.note import Note
from epii.view.buttons.nav_buttons import LeftNoteButton, RightNoteButton
from epii.view.buttons.update_buttons import UpdateButton
from epii.view.view import Header, View, min_height, min_width
from epii.view_model.view_model import ViewModel
from tests.utils import note_1_data, note_2_data


@pytest.fixture(autouse=True)
def view():
    if not QApplication.instance():
        app = QApplication()
    else:
        app = QApplication.instance()
    controller = Controller(Mock(spec=ViewModel))
    viewmodel = Mock(spec=ViewModel)
    viewmodel.get_data.return_value = "Note Content 0"
    view = View(controller, viewmodel)
    yield view
    app.quit()
    del app


def test_init_ui(view):
    assert view.minimumWidth() == min_width
    assert view.minimumHeight() == min_height
    assert view.windowTitle() == "epii"
    assert isinstance(view.centralWidget(), QWidget)
    assert isinstance(view.centralWidget().layout(), QVBoxLayout)
    assert isinstance(view.centralWidget().layout().itemAt(0).widget(), Header)
    assert isinstance(view.centralWidget().layout().itemAt(1).widget(), UpdateButton)
    assert isinstance(view.centralWidget().layout().itemAt(2).widget(), LeftNoteButton)
    assert isinstance(view.centralWidget().layout().itemAt(3).widget(), RightNoteButton)
    assert view.centralWidget().layout().count() == 4


def test_header_init_ui():
    viewmodel = Mock(spec=ViewModel)
    view_data_return = "Note Content 0"
    viewmodel.get_data.return_value = view_data_return
    header = Header(viewmodel)
    assert header.text() == view_data_return


def test_increment_note_button_init_ui():
    controller = Mock(spec=Controller)
    button = UpdateButton(controller)
    assert button.text() == "Increment"


def test_left_note_button_init_ui():
    controller = Mock(spec=Controller)
    button = LeftNoteButton(controller)
    assert button.text() == "Left"


def test_right_note_button_init_ui():
    controller = Mock(spec=Controller)
    button = RightNoteButton(controller)
    assert button.text() == "Right"


def test_header_update_text_on_emit():
    viewmodel = ViewModel(Model([Note(**note_1_data)]))

    header = Header(viewmodel)

    spy = QSignalSpy(viewmodel.data_changed)

    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 0"
    assert spy.count() == 0

    with patch("epii.view_model.ViewModel.get_data") as mock_get_data:
        new_data = "New Note Content"
        mock_get_data.return_value = new_data
        viewmodel.data_changed.emit()

        assert header.text() == new_data


def test_header_update_text_on_button_press():
    viewmodel = ViewModel(Model([Note(**note_1_data)]))
    controller = Controller(viewmodel)

    header = Header(viewmodel)
    update_button = UpdateButton(controller)

    spy = QSignalSpy(viewmodel.data_changed)

    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 0"
    assert spy.count() == 0

    QTest.mouseClick(update_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 1"
    assert spy.count() == 1

    with patch("epii.view_model.ViewModel.get_data") as mock_get_data:
        new_data = "New Note Content"
        mock_get_data.return_value = new_data
        viewmodel.data_changed.emit()

        assert header.text() == new_data


def test_header_switch_note_on_button_press():
    viewmodel = ViewModel(Model([Note(**note_1_data), Note(**note_2_data)]))
    controller = Controller(viewmodel)

    header = Header(viewmodel)
    left_button = LeftNoteButton(controller)
    right_button = RightNoteButton(controller)

    spy = QSignalSpy(viewmodel.data_changed)

    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 0"
    assert spy.count() == 0

    QTest.mouseClick(right_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_2_data['content']} 0"
    assert spy.count() == 1

    QTest.mouseClick(left_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 0"
    assert spy.count() == 2

    QTest.mouseClick(left_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 0"
    assert spy.count() == 3

    QTest.mouseClick(right_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_2_data['content']} 0"
    assert spy.count() == 4

    QTest.mouseClick(right_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_2_data['content']} 0"
    assert spy.count() == 5


def test_header_update_notes_individually_on_button_press():
    viewmodel = ViewModel(Model([Note(**note_1_data), Note(**note_2_data)]))
    controller = Controller(viewmodel)

    header = Header(viewmodel)
    left_button = LeftNoteButton(controller)
    right_button = RightNoteButton(controller)
    update_button = UpdateButton(controller)

    spy = QSignalSpy(viewmodel.data_changed)

    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 0"
    assert spy.count() == 0

    QTest.mouseClick(update_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 1"
    assert spy.count() == 1

    QTest.mouseClick(right_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_2_data['content']} 0"
    assert spy.count() == 2

    QTest.mouseClick(left_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 1"
    assert spy.count() == 3

    QTest.mouseClick(update_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_1_data['content']} 2"
    assert spy.count() == 4

    QTest.mouseClick(right_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_2_data['content']} 0"
    assert spy.count() == 5

    QTest.mouseClick(update_button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_2_data['content']} 1"
    assert spy.count() == 6
