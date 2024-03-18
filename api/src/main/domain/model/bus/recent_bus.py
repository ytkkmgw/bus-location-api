from pydantic import BaseModel

from domain.model.bus.bus import Bus
from domain.model.bus.now_location import NowLocation


class RecentBus(BaseModel):
    """直近で到着するバス便"""

    bus: Bus
    now_location: NowLocation

    def __init__(self, bus: Bus, now_location: NowLocation):
        super().__init__(bus=bus, now_location=now_location)
