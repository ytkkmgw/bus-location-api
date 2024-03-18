from abc import ABC, abstractmethod

from domain.model.busstop.busstops import Busstops
from domain.model.route.route_identifier import RouteIdentifier


class BusstopRepository(ABC):
    @abstractmethod
    def list_all(self, route_identifier: RouteIdentifier) -> Busstops:
        pass
