import requests

from config.api.odpt_api_endpoint import OdptAPIEndpoint
from domain.model.bus.bus import Bus
from domain.model.bus.bus_identifier import BusIdentifier
from domain.model.bus.buses import Buses
from domain.model.bus.departure_time import DepartureTime
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstop_identifier import BusstopIdentifier
from domain.model.route.bus_route import BusRoute
from domain.policy.unsupported_operation_error import UnsupportedOperationError

from usecase.repository.bus.bus_repository import BusRepository


class BusDataSource(BusRepository):
    def __init__(self):
        self.requests = requests

    def current(self, bus_route: BusRoute, base_busstop: Busstop) -> Buses:
        query = {"odpt:busroutePattern": bus_route.identifier.value}
        url = OdptAPIEndpoint("https://api.odpt.org/api/v4/odpt:Bus", query)
        responses: list[dict] = self.requests.get(url.create()).json()
        if len(responses) == 0:
            return Buses.create_empty()

        buses: list[Bus] = []
        for response in responses:
            bus_identifier: BusIdentifier = BusIdentifier(response["odpt:busTimetable"])
            # TODO なぜかtimetableがnullになるレコードがある。原因不明だが、一旦はリストから外す。
            if bus_identifier is None:
                continue
            buses.append(
                Bus(
                    bus_identifier,
                    self._get_depature_time(bus_identifier, base_busstop),
                    self._create_busstop(response.get("odpt:fromBusstopPole"), bus_route),
                    self._create_busstop(response["odpt:toBusstopPole"], bus_route),
                )
            )

        return Buses(buses)

    def _get_depature_time(
        self, bus_identifier: BusIdentifier, base_busstop: Busstop
    ) -> DepartureTime:

        query = {"owl:sameAs": bus_identifier.value}
        url = OdptAPIEndpoint("https://api.odpt.org/api/v4/odpt:BusTimetable", query)

        response: [dict] = self.requests.get(url.create()).json()[0]
        for entity in response["odpt:busTimetableObject"]:
            busstop_identifier = BusstopIdentifier(entity["odpt:busstopPole"])
            if base_busstop.identifier.__eq__(busstop_identifier):
                return DepartureTime(entity["odpt:departureTime"])
        raise UnsupportedOperationError("出発時刻が見つからない")

    @staticmethod
    def _create_busstop(identifier_value: str, bus_route: BusRoute) -> Busstop:
        busstop_identifier = BusstopIdentifier(identifier_value)
        busstop = bus_route.busstops.get_of_busstop_identifier(busstop_identifier)
        if busstop is None:
            return Busstop.create_empty()
        return Busstop(
            busstop_identifier,
            busstop.name,
            busstop.number,
        )
