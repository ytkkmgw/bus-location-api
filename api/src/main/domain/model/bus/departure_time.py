from datetime import time

from pydantic import BaseModel


class DepartureTime(BaseModel):
    """出発時刻"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)
