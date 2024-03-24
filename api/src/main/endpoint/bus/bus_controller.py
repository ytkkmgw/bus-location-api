import fastapi
from fastapi.params import Depends

from domain.model.busstop.busstop_name import BusstopName
from domain.model.pole.busstop_poles import BusstopPoles
from endpoint.bus.response.bus_location_response import BusLocationResponse
from endpoint.bus.response.bus_route_response import BusRouteResponse
from endpoint.bus.response.busstop_pole_response import BusStopPoleResponse
from usecase.service.bus.bus_service import BusService
from usecase.service.pole.pole_service import PoleService

router = fastapi.APIRouter(prefix="/bus", tags=["サンプル"])


@router.get("/")
def get(
    name: str,
    pole_service: PoleService = Depends(),
    bus_service: BusService = Depends(),
):
    busstop_name = BusstopName(name)
    poles: BusstopPoles = pole_service.list_all(busstop_name)
    busstop_pole_responses: list[BusStopPoleResponse] = []
    for pole in poles.as_list():
        bus_route_responses: list[BusRouteResponse] = []
        for busroute in pole.bus_routes.as_list():
            busstop = busroute.busstops.get_of_name(busstop_name)
            recent_bus = bus_service.recent(busroute, busstop)
            bus_route_responses.append(BusRouteResponse(busroute, recent_bus))
        busstop_pole_responses.append(BusStopPoleResponse(pole, bus_route_responses))

    return BusLocationResponse(busstop_name, busstop_pole_responses)


@router.get("/check")
def check_busstio(name: str, pole_service: PoleService = Depends()):
    busstop_name = BusstopName(name)
    if pole_service.find_by(busstop_name):
        # raise ResourceNotFoundError("")
        return False
    return True
