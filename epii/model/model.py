from typing import List

from epii.notes.note import Note


class Model:
    def __init__(self, notes: List[Note]) -> None:
        self.data = notes
        self.idx = 0

    def change_idx(self, direction: int) -> None:
        if self.idx + direction < 0 or self.idx + direction >= len(self.data):
            return
        self.idx += direction

    def get_data(self) -> list[Note]:
        return self.data

    def get_current_note(self) -> Note:
        return self.data[self.idx]

    def update_data(self, notes: List[Note]) -> None:
        note = notes[self.idx]
        updated_note = note.model_copy(
            update={"count": note.count + 1, "content": f"{note.content}"}
        )
        # For now we are using the idx to update the note, but in the future we
        # should use the note id.
        self.data = [
            updated_note if i == self.idx else note for i, note in enumerate(notes)
        ]
