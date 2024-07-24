from unittest.mock import Mock, patch

import pytest
from PySide6.QtCore import Qt
from PySide6.QtTest import QSignalSpy, QTest
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from utils import note_data

from epii.controller.controller import Controller
from epii.model.model import Model
from epii.notes.note import Note
from epii.view.view import Button, Header, View, min_height, min_width
from epii.view_model.view_model import ViewModel


@pytest.fixture
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
    assert isinstance(view.centralWidget().layout().itemAt(1).widget(), Button)


def test_header_init_ui():
    viewmodel = Mock(spec=ViewModel)
    view_data_return = "Note Content 0"
    viewmodel.get_data.return_value = view_data_return
    header = Header(viewmodel)
    assert header.text() == view_data_return


def test_button_init_ui():
    controller = Mock(spec=Controller)
    button = Button(controller)
    assert button.text() == "Increment"


def test_header_update_text_on_button_press():
    viewmodel = ViewModel(Model([Note(**note_data)]))
    controller = Controller(viewmodel)

    header = Header(viewmodel)
    button = Button(controller)

    spy = QSignalSpy(viewmodel.data_changed)

    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_data['content']} 0"
    assert spy.count() == 0

    QTest.mouseClick(button, Qt.LeftButton)
    assert header.text() == viewmodel.get_data()
    assert header.text() == f"{note_data['content']} 1"
    assert spy.count() == 1

    with patch("epii.view_model.ViewModel.get_data") as mock_get_data:
        new_data = "New Note Content"
        mock_get_data.return_value = new_data
        viewmodel.data_changed.emit()

        assert header.text() == new_data
