from pydantic import BaseModel


class BusIdentifier(BaseModel):
    """バス便識別子"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)
