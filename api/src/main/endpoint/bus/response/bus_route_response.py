from pydantic import BaseModel

from domain.model.bus.departure_time import DepartureTime
from domain.model.bus.now_location import NowLocation
from domain.model.bus.recent_bus import RecentBus
from domain.model.route.bus_route import BusRoute
from domain.model.route.destination import Destination
from domain.model.route.route_number import RouteNumber


class BusRouteResponse(BaseModel):
    route_number: RouteNumber
    destination: Destination
    recent_departure: DepartureTime
    now_location: NowLocation

    def __init__(self, bus_route: BusRoute, recent_bus: RecentBus):
        super().__init__(
            route_number=bus_route.number,
            destination=bus_route.destination,
            recent_departure=recent_bus.bus.departure_time,
            now_location=recent_bus.now_location,
        )
