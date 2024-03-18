from pydantic import BaseModel

from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstop_identifier import BusstopIdentifier
from domain.model.busstop.busstop_number import BusstopNumber
from domain.policy.resource_notfound_error import ResourceNotFoundError


class Busstops(BaseModel):
    """バス停一覧"""

    busstops: list[Busstop]

    def __init__(self, busstops: list[Busstop]):
        super().__init__(busstops=busstops)

    def get(self, busstop_identifier: BusstopIdentifier) -> Busstop:
        for busstop in self.busstops:
            if busstop.__eq__(busstop_identifier):
                return busstop
        raise ResourceNotFoundError("該当するバス停が無い")
