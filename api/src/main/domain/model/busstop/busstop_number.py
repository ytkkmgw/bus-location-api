from __future__ import annotations
from pydantic import BaseModel


class BusstopNumber(BaseModel):
    """バス停番号(起点からの連番)"""

    value: int

    def __init__(self, value: int):
        super().__init__(value=value)

    def is_first_departure(self) -> bool:
        return self.value == 0

    def is_停車中(self) -> bool:
        return self.value == 0

    def is_after(self, other: BusstopNumber) -> bool:
        return self.value > other.value

    def __sub__(self, other: BusstopNumber) -> BusstopNumber:
        return BusstopNumber(self.value - other.value)
