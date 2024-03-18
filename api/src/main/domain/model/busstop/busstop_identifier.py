from pydantic import BaseModel


class BusstopIdentifier(BaseModel):
    """バス停識別子"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)
