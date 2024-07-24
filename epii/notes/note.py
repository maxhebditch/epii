from datetime import datetime
from pathlib import Path
from typing import Optional
from uuid import UUID

import yaml
from pydantic import BaseModel
from pydantic.networks import HttpUrl

YAML_FILE = "example.yaml"
BASE_DIR = Path(__file__).parent


class Note(BaseModel, frozen=True):
    uuid: UUID
    date: datetime
    content: str
    url: Optional[HttpUrl] = None
    source: Optional[str] = None
    count: int = 0


def read_notes_from_yaml() -> list[Note]:
    yaml_file_path = BASE_DIR / YAML_FILE
    with yaml_file_path.open(mode="r") as notes_file:
        yaml_data = yaml.safe_load(notes_file)
        notes = []
        for uuid, body in yaml_data.items():
            notes.append(Note(uuid=uuid, **body))

        return notes


notes = read_notes_from_yaml()
