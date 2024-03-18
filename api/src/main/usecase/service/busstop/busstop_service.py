from fastapi.params import Depends

from config.di.inject import inject
from domain.model.route.route_identifier import RouteIdentifier
from usecase.repository.busstop.busstop_repository import BusstopRepository


class BusstopService:
    def __init__(
        self, busstop_repository: BusstopRepository = Depends(inject(BusstopRepository))
    ):
        self.busstop_repository = busstop_repository

    def list_all(self, route_indentifier: RouteIdentifier):
        return self.busstop_repository.list_all(route_indentifier)
