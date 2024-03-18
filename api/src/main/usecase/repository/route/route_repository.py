from abc import ABC, abstractmethod

from domain.model.route.bus_routes import BusRoutes
from domain.model.route.route_identifier import RouteIdentifier


class RouteRepository(ABC):
    @abstractmethod
    def list_all(self, route_identifier: RouteIdentifier) -> BusRoutes:
        pass
