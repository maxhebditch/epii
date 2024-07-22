from datetime import datetime
from uuid import UUID

from pydantic.networks import HttpUrl

note_data = {
    "uuid": UUID("57ded2b6-8c21-45ba-b194-4334cb81b16b"),
    "date": datetime.fromisoformat("2023-06-15T08:51:25.103Z"),
    "url": HttpUrl("https://example.com"),
    "content": """
    The actual content of the note. It can be any text or information
    """,
    "source": "The internet",
}
