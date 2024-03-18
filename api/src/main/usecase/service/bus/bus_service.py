from fastapi.params import Depends

from config.di.inject import inject
from domain.model.route.bus_route import BusRoute
from usecase.repository.bus.bus_repository import BusRepository


class BusService:
    def __init__(self, bus_repository=Depends(inject(BusRepository))):
        self.bus_repository = bus_repository

    def current(self, bus_route: BusRoute):
        pass
