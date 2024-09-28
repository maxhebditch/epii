from datetime import datetime
from uuid import UUID

from pydantic.networks import HttpUrl

note_1_data = {
    "uuid": UUID("57ded2b6-8c21-45ba-b194-4334cb81b16b"),
    "date": datetime.fromisoformat("2023-06-15T08:51:25.103Z"),
    "url": HttpUrl("https://example.com"),
    "content": """
    The actual content of the note. It can be any text or information
    """,
    "source": "The internet",
}

note_2_data = {
    "uuid": UUID("e38e841e-8310-4d2e-a69f-4b1642d72016"),
    "date": datetime.fromisoformat("2024-01-01T00:00:00.000Z"),
    "content": """
    A second note about something else
    """,
    "source": "A book",
}
