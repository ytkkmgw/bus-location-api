import requests

from injector import inject

from config.api.odpt_api_endpoint import OdptAPIEndpoint
from domain.model.busstop.busstop_name import BusstopName
from domain.model.pole.busstop_platform import BusstopPlatform
from domain.model.pole.busstop_pole import BusstopPole
from domain.model.pole.busstop_pole_number import BusstopPoleNumber
from domain.model.pole.busstop_poles import BusstopPoles
from domain.model.route.route_identifier import RouteIdentifier
from domain.model.route.route_identifiers import RouteIdentifiers
from usecase.repository.pole.pole_repository import PoleRepository
from usecase.repository.route.route_repository import RouteRepository


class PoleDatasource(PoleRepository):
    @inject
    def __init__(self, route_repository: RouteRepository):
        self.requests = requests
        self.route_repository = route_repository

    def list_all(self, busstop_name: BusstopName) -> BusstopPoles:
        query = {"dc:title": busstop_name.value}
        url = OdptAPIEndpoint("https://api.odpt.org/api/v4/odpt:BusstopPole", query)

        responses: list[dict] = self.requests.get(url.create()).json()
        poles: list[BusstopPole] = []
        for response in responses:
            route_identifiers = self._create_busroute_identifier(
                response["odpt:busroutePattern"]
            )
            bus_routes = self.route_repository.list_all(route_identifiers)
            busstop_pole = BusstopPole(
                BusstopPoleNumber(response["odpt:busstopPoleNumber"]),
                BusstopPlatform(response.get("odpt:platformNumber")),
                bus_routes,
            )
            poles.append(busstop_pole)
        return BusstopPoles(poles)

    @staticmethod
    def _create_busroute_identifier(identifier_list: list[str]) -> RouteIdentifiers:
        identifiers = []
        for value in identifier_list:
            identifiers.append(RouteIdentifier(value))
        return RouteIdentifiers(identifiers)

    def find_by(self, busstop_name: BusstopName) -> bool:
        query = {"dc:title": busstop_name.value}
        url = OdptAPIEndpoint("https://api.odpt.org/api/v4/odpt:BusstopPole", query)
        responses: list[dict] = self.requests.get(url.create()).json()
        print(responses)
        return len(responses) == 0
