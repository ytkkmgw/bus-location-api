from pydantic import BaseModel

from domain.model.busstop.busstops import Busstops
from domain.model.route.destination import Destination
from domain.model.route.route_identifier import RouteIdentifier
from domain.model.route.route_number import RouteNumber


class BusRoute(BaseModel):
    """バス運行系統"""

    identifier: RouteIdentifier
    number: RouteNumber
    destination: Destination
    busstops: Busstops

    def __init__(
        self,
        identifier: RouteIdentifier,
        number: RouteNumber,
        destination: Destination,
        busstops: Busstops,
    ):
        super().__init__(
            identifier=identifier,
            number=number,
            destination=destination,
            busstops=busstops,
        )
