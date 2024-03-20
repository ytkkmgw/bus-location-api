from fastapi.params import Depends

from config.di.inject import inject
from domain.model.busstop.busstop_name import BusstopName
from domain.model.pole.busstop_poles import BusstopPoles
from usecase.repository.pole.pole_repository import PoleRepository


class PoleService:
    def __init__(
        self, pole_repository: PoleRepository = Depends(inject(PoleRepository))
    ):
        self.pole_repository = pole_repository

    def list_all(self, busstop_name: BusstopName) -> BusstopPoles:
        return self.pole_repository.list_all(busstop_name)