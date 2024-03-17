from pydantic import BaseModel

from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstop_number import BusstopNumber


class Busstops(BaseModel):
    """バス停一覧"""

    busstops: list[Busstop]

    def __init__(self, busstops: list[Busstop]):
        super().__init__(busstops=busstops)

    def get_number(self, busstop: Busstop) -> BusstopNumber:
        return BusstopNumber(self.list.index(busstop))
