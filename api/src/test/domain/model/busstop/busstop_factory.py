from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstop_name import BusstopName
from domain.model.busstop.busstop_number import BusstopNumber


class BusstopFactory:
    @staticmethod
    def create(busstop_name: str, busstop_number: int) -> Busstop:
        return Busstop(BusstopName(busstop_name), BusstopNumber(busstop_number))

    @staticmethod
    def empty_create():
        return Busstop.create_empty()
