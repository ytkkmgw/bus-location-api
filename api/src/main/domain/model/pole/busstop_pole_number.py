from pydantic import BaseModel


class BusstopPoleNumber(BaseModel):
    """バス停標柱番号"""

    value: int

    def __init__(self, value: int):
        super().__init__(value=value)
