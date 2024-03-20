from pydantic import BaseModel

from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstop_identifier import BusstopIdentifier
from domain.model.busstop.busstop_name import BusstopName
from domain.policy.resource_notfound_error import ResourceNotFoundError


class Busstops(BaseModel):
    """バス停一覧"""

    busstops: list[Busstop]

    def __init__(self, busstops: list[Busstop]):
        super().__init__(busstops=busstops)

    def get_of_busstop_identifier(
        self, identifier: BusstopIdentifier
    ) -> Busstop | None:
        for busstop in self.busstops:
            if busstop.__eq__(other_identifier=identifier):
                return busstop
        return None

    def get_of_name(self, name: BusstopName) -> Busstop:
        for busstop in self.busstops:
            if busstop.__eq__(other_name=name):
                return busstop
        raise ResourceNotFoundError("該当するバス停が無い")
