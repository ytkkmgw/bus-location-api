from abc import ABC, abstractmethod

from domain.model.bus.bus_identifier import BusIdentifier
from domain.model.bus.departure_time import DepartureTime
from domain.model.busstop.busstop_identifier import BusstopIdentifier


class BusTimetableRepository(ABC):
    @abstractmethod
    def find_by(
        self, bus_identifier: BusIdentifier, busstop_identifier: BusstopIdentifier
    ) -> DepartureTime:
        pass
