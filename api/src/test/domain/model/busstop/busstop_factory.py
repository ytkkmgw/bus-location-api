from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstop_identifier import BusstopIdentifier
from domain.model.busstop.busstop_name import BusstopName
from domain.model.busstop.busstop_number import BusstopNumber


class BusstopFactory:
    @staticmethod
    def create(
        busstop_identifier: str, busstop_name: str, busstop_number: int
    ) -> Busstop:
        return Busstop(
            BusstopIdentifier(busstop_identifier),
            BusstopName(busstop_name),
            BusstopNumber(busstop_number),
        )

    @staticmethod
    def create_empty():
        return Busstop.create_empty()
