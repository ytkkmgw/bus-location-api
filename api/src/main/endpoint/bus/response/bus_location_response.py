from pydantic import BaseModel

from domain.model.busstop.busstop_name import BusstopName
from endpoint.bus.response.busstop_pole_response import BusStopPoleResponse


class BusLocationResponse(BaseModel):
    busstop_name: BusstopName
    poles: list[BusStopPoleResponse]

    def __init__(self, busstop_name: BusstopName, poles: list[BusStopPoleResponse]):
        super().__init__(busstop_name=busstop_name, poles=poles)
