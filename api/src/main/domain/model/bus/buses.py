from __future__ import annotations
from pydantic import BaseModel

from domain.model.bus.bus import Bus
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstops import Busstops


class Buses(BaseModel):
    """バス便一覧"""

    buses: list[Bus]

    def __init__(self, buses: list[Bus]):
        super().__init__(buses=buses)

    def as_list(self) -> list[Bus]:
        return self.buses

    def is_empty(self) -> bool:
        return len(self.buses) == 0

    def reverse(self) -> Buses:
        new_list = self.buses.copy()
        new_list.reverse()
        return Buses(new_list)

    def recent_bus(self, base_busstop: Busstop, busstops: Busstops) -> Bus | None:
        # 始発停留所(index=0)の場合は位置情報が無い
        # busesの要素が空の場合(本日の運行が終了している)は位置情報が無い
        if self.is_empty() or base_busstop.number.is_first_departure():
            return None

        for bus in self.reverse().as_list():
            if bus.is_after(base_busstop):
                continue
            return bus
