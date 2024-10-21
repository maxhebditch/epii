from threading import Lock, Thread
from unittest.mock import Mock

import pytest
from PySide6.QtTest import QSignalSpy

from epii.model.model import Model
from epii.model.notes.note import Note
from epii.view_model.direction import Direction
from epii.view_model.view_model import ViewModel
from tests.utils import note_1_data


@pytest.fixture
def view_model():
    return ViewModel(Model([Note(**note_1_data)]))


def test_get_notes_all_returns_data_no_emit(view_model):
    expected_data = f"{note_1_data["content"]} 0"

    spy = QSignalSpy(view_model.data_changed)
    observed_data = view_model.get_notes_all()
    assert expected_data == observed_data
    assert spy.count() == 0


def test_get_notes_all_calls_model_get():
    mock_model = Mock(spec=Model)
    mock_model.data = Note(**note_1_data)
    view_mocked_model = ViewModel(mock_model)
    view_mocked_model.get_notes_all()
    view_mocked_model._model.get_active_item.assert_called_once()


def test_update_note_current_no_return_only_emits(view_model):
    mock_model = Mock(spec=Model)
    mock_model.data = Note(**note_1_data)
    spy = QSignalSpy(view_model.data_changed)

    update_return = view_model.update_note_current()
    assert update_return is None
    assert spy.count() == 1


def test_update_note_current_calls_model_update():
    mock_model = Mock(spec=Model)
    mock_model.data = Note(**note_1_data)
    view_mocked_model = ViewModel(mock_model)
    view_mocked_model.update_note_current()
    view_mocked_model._model.update_data.assert_called_once()


def test_change_idx_left():
    mock_model = Mock(spec=Model)
    mock_model.data = Note(**note_1_data)
    view_mocked_model = ViewModel(mock_model)
    view_mocked_model.change_note_current(Direction.LEFT)
    view_mocked_model._model.change_idx.assert_called_once_with(Direction.LEFT.value)


def test_change_idx_right():
    mock_model = Mock(spec=Model)
    mock_model.data = Note(**note_1_data)
    view_mocked_model = ViewModel(mock_model)
    view_mocked_model.change_note_current(Direction.RIGHT)
    view_mocked_model._model.change_idx.assert_called_once_with(Direction.RIGHT.value)


def test_update_view():
    mock_model = Mock(spec=Model)
    mock_model.data = Note(**note_1_data)
    view_mocked_model = ViewModel(mock_model)
    spy = QSignalSpy(view_mocked_model.data_changed)
    view_mocked_model.update_view()
    assert spy.count() == 1


update_lock = Lock()


@pytest.mark.parametrize("num_jobs, num_threads", [(98, 10), (200, 5), (50, 20)])
def test_concurrent_updates(view_model, num_jobs, num_threads):
    spy = QSignalSpy(view_model.data_changed)

    def update_note_current_concurrently() -> None:
        for _ in range(num_jobs):
            with update_lock:
                view_model.update_note_current()

    threads = [Thread(target=update_note_current_concurrently) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    expected_output = f"{note_1_data['content']} {num_threads * num_jobs}"
    observed_output = view_model.get_notes_all()
    assert observed_output == expected_output
    assert spy.count() == num_threads * num_jobs
