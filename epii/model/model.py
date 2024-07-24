from typing import List

from epii.notes.note import Note


class Model:
    def __init__(self, notes: List[Note]) -> None:
        self.data = notes

    def get_data(self) -> str:
        note = self.data[0]
        return f"{note.content} {note.count}"

    def update_data(self, notes: List[Note]) -> None:
        note = notes[0]
        updated_note = note.model_copy(
            update={"count": note.count + 1, "content": f"{note.content}"}
        )
        self.data = [updated_note]
