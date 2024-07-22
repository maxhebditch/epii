from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic.networks import HttpUrl


class Note(BaseModel, frozen=True):
    uuid: UUID
    date: datetime
    content: str
    url: Optional[HttpUrl] = None
    source: Optional[str] = None
    count: int = 0


notes = [
    Note(
        uuid=UUID("57ded2b6-8c21-45ba-b194-4334cb81b16b"),
        date=datetime.fromisoformat("2023-06-15T08:51:25.103Z"),
        url=HttpUrl("https://example.com"),
        content="""
        The actual content of the note. It can be any text or information
        """,
    )
]
