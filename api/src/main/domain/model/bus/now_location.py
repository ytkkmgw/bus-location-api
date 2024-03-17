from __future__ import annotations
from enum import Enum

from domain.model.bus.bus import Bus
from domain.model.bus.buses import Buses
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstops import Busstops


class NowLocation(Enum):
    """現在位置"""

    NONE = "位置情報無し"
    NOW = "現在地に到着"
    SOON = "まもなく到着"
    ONE = "1つ前に停車中"
    ONE_TWO = "1つ前〜2つ前間を走行中"
    TWO = "2つ前に停車中"
    TWO_THREE = "2つ前〜3つ前間を走行中"
    THREE = "3つ前"
    THREE_FOUR = "3つ前〜4つ前間を走行中"
    FOUR = "4つ前"
    FOUR_FIVE = "4つ前〜5つ前間を走行中"
    FIVE = "5つ前"
    FIVE_BEFORE = "5つ前にも未到着"

    def get_location(
        self, base_busstop: Busstop, buses: Buses, busstops: Busstops
    ) -> NowLocation:
        resent_arrive_bus: Bus = buses.recent_bus(base_busstop, busstops)
        if resent_arrive_bus is None:
            return self.NONE

        subtract_number: int = base_busstop.from_busstop.number_subtract(
            resent_arrive_bus
        )
        if resent_arrive_bus.is_停車中():
            match subtract_number:
                case 0:
                    return self.NOW
                case 1:
                    return self.ONE
                case 2:
                    return self.TWO
                case 3:
                    return self.ONE
                case 4:
                    return self.FOUR
                case 5:
                    return self.FIVE
                case _:
                    return self.FIVE_BEFORE

        match subtract_number:
            case 1:
                return self.ONE_TWO
            case 2:
                return self.TWO_THREE
            case 3:
                return self.THREE_FOUR
            case 4:
                return self.FOUR_FIVE
            case _:
                return self.FIVE_BEFORE
