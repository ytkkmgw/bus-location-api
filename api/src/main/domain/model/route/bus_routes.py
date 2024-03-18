from pydantic import BaseModel

from domain.model.route.bus_route import BusRoute
from domain.model.route.route_identifier import RouteIdentifier


class BusRoutes(BaseModel):
    """バス運行系統一覧"""

    routes: list[BusRoute]

    def __init__(self, routes: list[BusRoute]):
        super().__init__(routes=routes)

    def as_identifier_list(self) -> list[RouteIdentifier]:
        identifiers: list[RouteIdentifier] = []
        for route in self.routes:
            identifiers.append(route.identifier)
        return identifiers
