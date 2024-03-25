from injector import inject

from domain.model.bus.bus import Bus
from domain.model.bus.buses import Buses
from domain.model.bus.now_location import NowLocation
from domain.model.bus.recent_bus import RecentBus
from domain.model.busstop.busstop import Busstop
from domain.model.route.bus_route import BusRoute
from usecase.repository.bus.bus_repository import BusRepository


class BusService:
    @inject
    def __init__(self, bus_repository: BusRepository):
        self.bus_repository = bus_repository

    def recent(self, bus_route: BusRoute, base_busstop: Busstop) -> RecentBus:
        buses: Buses = self.bus_repository.current(bus_route, base_busstop)
        if len(buses.as_list()) == 0:
            return RecentBus.create_empty()
        recent_bus: Bus = buses.recent_bus(base_busstop)
        if recent_bus is None:
            return RecentBus.create_empty()
        return RecentBus(recent_bus, NowLocation.get_location(recent_bus, base_busstop))
