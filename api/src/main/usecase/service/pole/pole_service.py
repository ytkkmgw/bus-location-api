from injector import inject

from domain.model.busstop.busstop_name import BusstopName
from domain.model.pole.busstop_poles import BusstopPoles
from usecase.repository.pole.pole_repository import PoleRepository


class PoleService:
    @inject
    def __init__(self, pole_repository: PoleRepository):
        self.pole_repository = pole_repository

    def list_all(self, busstop_name: BusstopName) -> BusstopPoles:
        return self.pole_repository.list_all(busstop_name)

    def find_by(self, busstop_name: BusstopName) -> bool:
        return self.pole_repository.find_by(busstop_name)
