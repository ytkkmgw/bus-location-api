from pydantic import BaseModel

from domain.model.pole.busstop_pole import BusstopPole


class BusstopPoles(BaseModel):
    """バス停標柱一覧"""

    poles: list[BusstopPole]

    def __init__(self, poles: list[BusstopPole]):
        super().__init__(poles=poles)

    def as_list(self):
        return self.poles
