from __future__ import annotations
from pydantic import BaseModel

from domain.model.bus.bus_identifier import BusIdentifier
from domain.model.bus.departure_time import DepartureTime
from domain.model.busstop.busstop import Busstop


class Bus(BaseModel):
    """バス便"""

    identifier: BusIdentifier
    departure_time: DepartureTime
    from_busstop: Busstop
    to_busstop: Busstop

    def __init__(
        self,
        identifier: BusIdentifier,
        departure_time: DepartureTime,
        from_busstop: Busstop,
        to_busstop: Busstop,
    ):
        super().__init__(
            identifier=identifier,
            departure_time=departure_time,
            from_busstop=from_busstop,
            to_busstop=to_busstop,
        )

    def is_停車中(self) -> bool:
        return self.to_busstop.is_停車中()

    def is_after(self, base: Busstop) -> bool:
        if self.to_busstop.is_停車中():
            return self.from_busstop.is_after(base)
        return self.to_busstop.is_after(base)
