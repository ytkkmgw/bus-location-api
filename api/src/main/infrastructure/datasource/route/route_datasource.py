import requests

from config.api.odpt_api_endpoint import OdptAPIEndpoint
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstop_identifier import BusstopIdentifier
from domain.model.busstop.busstop_name import BusstopName
from domain.model.busstop.busstop_number import BusstopNumber
from domain.model.busstop.busstops import Busstops
from domain.model.route.bus_route import BusRoute
from domain.model.route.bus_routes import BusRoutes
from domain.model.route.destination import Destination
from domain.model.route.route_identifier import RouteIdentifier
from domain.model.route.route_identifiers import RouteIdentifiers
from domain.model.route.route_number import RouteNumber

from usecase.repository.route.route_repository import RouteRepository


class RouteDatasource(RouteRepository):
    def __init__(self):
        self.requests = requests

    def list_all(self, route_identifiers: RouteIdentifiers) -> BusRoutes:
        query = {"owl:sameAs": ",".join(route_identifiers.as_str_list())}
        url = OdptAPIEndpoint("https://api.odpt.org/api/v4/odpt:BusroutePattern", query)
        responses: list[dict] = self.requests.get(url.create()).json()

        busstop_list: list[BusRoute] = []
        for response in responses:
            route_identifier = RouteIdentifier(response["owl:sameAs"])
            route_number = RouteNumber(response["dc:title"])
            destination = Destination(response["odpt:note"].split(":")[1])
            busstops = self._create_busstops(response["odpt:busstopPoleOrder"])
            busstop_list.append(
                BusRoute(route_identifier, route_number, destination, busstops)
            )
        return BusRoutes(busstop_list)

    @staticmethod
    def _create_busstops(busstop_list: list[dict]) -> Busstops:
        busstops: list[Busstop] = []
        for busstop in busstop_list:
            busstops.append(
                Busstop(
                    BusstopIdentifier(busstop["odpt:busstopPole"]),
                    BusstopName(busstop["odpt:note"].split(":")[0]),
                    BusstopNumber(busstop["odpt:index"]),
                )
            )
        return Busstops(busstops)
