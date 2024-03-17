from pydantic import BaseModel

from domain.model.pole.busstop_platform import BusstopPlatform
from domain.model.pole.busstop_pole_number import BusstopPoleNumber
from domain.model.route.bus_routes import BusRoutes


class BusstopPole(BaseModel):
    """バス停標柱"""

    pole_number: BusstopPoleNumber
    platform: BusstopPlatform
    bus_routes: BusRoutes

    def __init__(
        self,
        pole_number: BusstopPoleNumber,
        platform: BusstopPlatform,
        bus_routes: BusRoutes,
    ):
        super().__init__(
            pole_number=pole_number, platform=platform, bus_routes=bus_routes
        )
