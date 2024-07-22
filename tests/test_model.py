from utils import note_data

from epii.model.model import Model
from epii.model.note import Note


def test_model_get_data():
    note = Note(**note_data)
    model = Model([note])

    assert model.get_data() == f"{note.content} {note.count}"


def test_model_update_data():
    note = Note(**note_data)
    model = Model([note])

    model.update_data([note])
    expected_note_1 = Note(**{**note_data, "count": 1})
    observed_note_1 = model.data[0]
    assert observed_note_1 == expected_note_1
    assert observed_note_1 is not expected_note_1

    model.update_data([expected_note_1])
    expected_note_2 = Note(**{**note_data, "count": 2})
    observed_note_2 = model.data[0]
    assert observed_note_2 == expected_note_2
    assert observed_note_2 is not expected_note_2
