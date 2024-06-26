from __future__ import annotations
from enum import Enum

from domain.model.bus.bus import Bus
from domain.model.busstop.busstop import Busstop


class NowLocation(Enum):
    """現在位置"""

    NONE = "位置情報無し"
    NOW = "現在地に到着"
    SOON = "まもなく到着"
    ONE = "1つ前に停車中"
    ONE_TWO = "1つ前〜2つ前間を走行中"
    TWO = "2つ前に停車中"
    TWO_THREE = "2つ前〜3つ前間を走行中"
    THREE = "3つ前に停車中"
    THREE_FOUR = "3つ前〜4つ前間を走行中"
    FOUR = "4つ前に停車中"
    FOUR_FIVE = "4つ前〜5つ前間を走行中"
    FIVE = "5つ前に停車中"
    FIVE_BEFORE = "5つ前にも未到着"

    @staticmethod
    def get_location(recent_bus: Bus, base_busstop: Busstop) -> NowLocation:
        if recent_bus is None:
            return NowLocation.NONE
        subtract_number: int = base_busstop.number_subtract(recent_bus.from_busstop)

        if recent_bus.is_停車中():
            match subtract_number:
                case 0:
                    return NowLocation.NOW
                case 1:
                    return NowLocation.ONE
                case 2:
                    return NowLocation.TWO
                case 3:
                    return NowLocation.ONE
                case 4:
                    return NowLocation.FOUR
                case 5:
                    return NowLocation.FIVE
                case _:
                    return NowLocation.FIVE_BEFORE

        match subtract_number:
            case 1:
                return NowLocation.SOON
            case 2:
                return NowLocation.ONE_TWO
            case 3:
                return NowLocation.TWO_THREE
            case 4:
                return NowLocation.THREE_FOUR
            case 5:
                return NowLocation.FOUR_FIVE
            case _:
                return NowLocation.FIVE_BEFORE
