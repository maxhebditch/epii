import pytest
from pydantic import ValidationError
from utils import note_data

from epii.notes.note import Note

defaults = ["uuid", "date", "content"]


def test_note_creation():
    note = Note(**note_data)

    assert note.uuid == note_data["uuid"]
    assert note.date == note_data["date"]
    assert note.url == note_data["url"]
    assert note.content == note_data["content"]
    assert note.source is note_data["source"]
    assert note.count == 0


def test_note_creation_pydantic_coercion():
    note_str_data = {k: str(v) for k, v in note_data.items()}
    note = Note(**note_str_data)

    assert note.uuid == note_data["uuid"]
    assert note.date == note_data["date"]
    assert note.url == note_data["url"]
    assert note.content == note_data["content"]
    assert note.source is note_data["source"]
    assert note.count == 0


def test_note_defaults():
    note_defaults_data = {k: note_data[k] for k in defaults}
    note = Note(**note_defaults_data)

    assert note.url is None
    assert note.source is None
    assert note.count == 0


def test_note_missing_defaults():
    for key in defaults:
        note_missing_data = {k: v for k, v in note_data.items() if k != key}
        with pytest.raises(ValidationError):
            Note(**note_missing_data)


def test_note_incorrect_type_coercion_uuid():
    for key in ["uuid", "date", "url"]:
        note_bad_coercion_data = {**note_data, key: "wrong"}

        with pytest.raises(ValidationError):
            Note(**note_bad_coercion_data)


def test_note_immutable():
    note = Note(**note_data)

    with pytest.raises(ValidationError):
        note.content = "This should raise an error"

    with pytest.raises(ValidationError):
        del note.content

    with pytest.raises(ValidationError):
        note.new_attribute = "No new attributes allowed"
