from injector import inject

from domain.model.route.bus_routes import BusRoutes
from domain.model.route.route_identifiers import RouteIdentifiers
from infrastructure.datasource.route.route_datasource import RouteDatasource


class RouteService:
    @inject
    def __init__(self, route_repository: RouteDatasource):
        self.route_repository = route_repository

    def list_all(self, route_identifiers: RouteIdentifiers) -> BusRoutes:
        return self.route_repository.list_all(route_identifiers)
