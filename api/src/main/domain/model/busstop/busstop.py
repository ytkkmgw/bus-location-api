from __future__ import annotations
from pydantic import BaseModel

from domain.model.busstop.busstop_name import BusstopName
from domain.model.busstop.busstop_number import BusstopNumber


class Busstop(BaseModel):
    """バス停"""

    name: BusstopName
    number: BusstopNumber

    def __init__(self, name: BusstopName, number: BusstopNumber):
        super().__init__(name=name, number=number)

    @staticmethod
    def create_empty():
        return Busstop(BusstopName(""), BusstopNumber(0))

    def is_停車中(self) -> bool:
        return self.name.is_停車中() and self.number.is_停車中()

    def is_after(self, other: Busstop) -> bool:
        return self.number.is_after(other.number)

    def is_現在地(self, other: Busstop) -> bool:
        return self.number.is_現在地(other.number)

    def number_subtract(self, other: Busstop) -> int:
        return self.number.__sub__(other.number).value
