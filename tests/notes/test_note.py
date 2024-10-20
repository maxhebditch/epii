import pytest
from pydantic import ValidationError

from epii.model.notes.note import Note
from tests.utils import note_1_data

defaults = ["uuid", "date", "content"]


def test_note_creation():
    note = Note(**note_1_data)

    assert note.uuid == note_1_data["uuid"]
    assert note.date == note_1_data["date"]
    assert note.url == note_1_data["url"]
    assert note.content == note_1_data["content"]
    assert note.source is note_1_data["source"]
    assert note.count == 0


def test_note_creation_pydantic_coercion():
    note_str_data = {k: str(v) for k, v in note_1_data.items()}
    note = Note(**note_str_data)

    assert note.uuid == note_1_data["uuid"]
    assert note.date == note_1_data["date"]
    assert note.url == note_1_data["url"]
    assert note.content == note_1_data["content"]
    assert note.source is note_1_data["source"]
    assert note.count == 0


def test_note_defaults():
    note_defaults_data = {k: note_1_data[k] for k in defaults}
    note = Note(**note_defaults_data)

    assert note.url is None
    assert note.source is None
    assert note.count == 0


def test_note_missing_defaults():
    for key in defaults:
        note_missing_data = {k: v for k, v in note_1_data.items() if k != key}
        with pytest.raises(ValidationError):
            Note(**note_missing_data)


def test_note_incorrect_type_coercion_uuid():
    for key in ["uuid", "date", "url"]:
        note_bad_coercion_data = {**note_1_data, key: "wrong"}

        with pytest.raises(ValidationError):
            Note(**note_bad_coercion_data)


def test_note_immutable():
    note = Note(**note_1_data)

    with pytest.raises(ValidationError):
        note.content = "This should raise an error"

    with pytest.raises(ValidationError):
        del note.content

    with pytest.raises(ValidationError):
        note.new_attribute = "No new attributes allowed"
