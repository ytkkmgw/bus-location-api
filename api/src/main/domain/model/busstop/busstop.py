from __future__ import annotations
from pydantic import BaseModel

from domain.model.busstop.busstop_identifier import BusstopIdentifier
from domain.model.busstop.busstop_name import BusstopName
from domain.model.busstop.busstop_number import BusstopNumber


class Busstop(BaseModel):
    """バス停"""

    identifier: BusstopIdentifier
    name: BusstopName
    number: BusstopNumber

    def __init__(
        self, identifier: BusstopIdentifier, name: BusstopName, number: BusstopNumber
    ):
        super().__init__(identifier=identifier, name=name, number=number)

    def is_停車中(self) -> bool:
        return self.name.is_停車中() and self.number.is_停車中()

    def is_after(self, other: Busstop) -> bool:
        return self.number.is_after(other.number)

    def number_subtract(self, other: Busstop) -> int:
        return self.number.__sub__(other.number).value

    def __eq__(self, other_identifier: BusstopIdentifier) -> bool:
        return self.identifier.__eq__(other_identifier)

    @staticmethod
    def create_empty():
        return Busstop(BusstopIdentifier(""), BusstopName(""), BusstopNumber(0))
