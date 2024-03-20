from pydantic import BaseModel

from domain.model.bus.bus import Bus
from domain.model.bus.bus_identifier import BusIdentifier
from domain.model.bus.departure_time import DepartureTime
from domain.model.bus.now_location import NowLocation
from domain.model.busstop.busstop import Busstop


class RecentBus(BaseModel):
    """直近で到着するバス便"""

    bus: Bus
    now_location: NowLocation

    def __init__(self, bus: Bus, now_location: NowLocation):
        super().__init__(bus=bus, now_location=now_location)

    @staticmethod
    def create_empty():
        return RecentBus(Bus.create_emtpy(), NowLocation.NONE)
