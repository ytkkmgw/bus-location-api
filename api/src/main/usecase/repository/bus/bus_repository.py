from abc import ABC, abstractmethod

from domain.model.bus.buses import Buses
from domain.model.busstop.busstop import Busstop
from domain.model.route.bus_route import BusRoute


class BusRepository(ABC):
    @abstractmethod
    def current(self, bus_route: BusRoute,base_busstop:Busstop) -> Buses:
        pass

