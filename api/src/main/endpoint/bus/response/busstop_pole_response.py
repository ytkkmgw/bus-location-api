from pydantic import BaseModel

from domain.model.pole.busstop_platform import BusstopPlatform
from domain.model.pole.busstop_pole import BusstopPole
from domain.model.pole.busstop_pole_number import BusstopPoleNumber
from endpoint.bus.response.bus_route_response import BusRouteResponse


class BusStopPoleResponse(BaseModel):
    pole_number: BusstopPoleNumber
    platform: BusstopPlatform
    routes: list[BusRouteResponse]

    def __init__(self, busstop_pole: BusstopPole, routes: list[BusRouteResponse]):
        super().__init__(
            pole_number=busstop_pole.pole_number,
            platform=busstop_pole.platform,
            routes=routes,
        )
