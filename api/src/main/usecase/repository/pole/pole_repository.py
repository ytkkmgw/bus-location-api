from abc import ABC, abstractmethod

from domain.model.busstop.busstop_name import BusstopName
from domain.model.pole.busstop_poles import BusstopPoles


class PoleRepository(ABC):
    @abstractmethod
    def list_all(self, busstop_name: BusstopName) -> BusstopPoles:
        pass

    @abstractmethod
    def find_by(self, busstop_name: BusstopName)->bool:
        pass
