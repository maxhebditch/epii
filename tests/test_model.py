from utils import note_1_data

from epii.model.model import Model
from epii.notes.note import Note


def test_model_initialisation():
    note = Note(**note_1_data)
    model = Model([note])

    assert model.data == [note]
    assert model.idx == 0


def test_model_get_data():
    note = Note(**note_1_data)
    model = Model([note])

    assert model.get_data() == [note]


def test_model_current_note():
    note = Note(**note_1_data)
    model = Model([note])

    assert model.get_current_note() == note


def test_model_change_idx():
    note = Note(**note_1_data)
    model = Model([note, note])

    model.change_idx(1)
    assert model.idx == 1

    model.change_idx(-1)
    assert model.idx == 0


def test_model_change_idx_limited_to_note_num():
    note = Note(**note_1_data)
    model = Model([note])

    model.change_idx(1)
    assert model.idx == 0


def test_model_change_idx_limited_to_positive():
    note = Note(**note_1_data)
    model = Model([note])

    model.change_idx(-1)
    assert model.idx == 0


def test_model_update_data():
    note = Note(**note_1_data)
    model = Model([note])

    model.update_data([note])
    expected_note_1 = Note(**{**note_1_data, "count": 1})
    observed_note_1 = model.data[0]
    assert observed_note_1 == expected_note_1
    assert observed_note_1 is not expected_note_1

    model.update_data([expected_note_1])
    expected_note_2 = Note(**{**note_1_data, "count": 2})
    observed_note_2 = model.data[0]
    assert observed_note_2 == expected_note_2
    assert observed_note_2 is not expected_note_2
