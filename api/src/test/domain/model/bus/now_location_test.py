"""現在位置テストケース"""
import pytest

from api.src.test.domain.model.busstop.busstop_factory import BusstopFactory
from api.src.test.domain.model.busstop.busstops_factory import BusstopsFactory
from domain.model.bus.bus import Bus
from domain.model.bus.bus_identifier import BusIdentifier
from domain.model.bus.buses import Buses
from domain.model.bus.departure_time import DepartureTime
from domain.model.bus.now_location import NowLocation
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstops import Busstops

buses: Buses = Buses(
    [
        Bus(
            BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
            DepartureTime("17:30"),
            BusstopFactory.create("サンロード入口", 1),
            BusstopFactory.create("東京女子大入口", 2),
        ),
        Bus(
            BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
            DepartureTime("17:00"),
            BusstopFactory.create("武蔵野寮前", 5),
            BusstopFactory.create_empty(),
        ),
    ]
)


@pytest.mark.parametrize(
    "busstop_name, busstop_number, excepted",
    [
        ("吉祥寺駅", 0, NowLocation.NONE),
        ("サンロード入口", 1, NowLocation.NONE),
        ("東京女子大入口", 2, NowLocation.SOON),
        ("武蔵野第四小学校", 3, NowLocation.ONE_TWO),
        ("立野町", 4, NowLocation.TWO_THREE),
        ("武蔵野寮前", 5, NowLocation.NOW),
        ("関町南二丁目", 6, NowLocation.ONE),
        ("東京三育小学校入口", 7, NowLocation.TWO),
    ],
)
def test_get_location(busstop_name, busstop_number, excepted):
    """バス停一覧・バス便一覧から現在位置を取得できる"""
    base_busstop: Busstop = BusstopFactory.create(busstop_name, busstop_number)
    busstops: Busstops = BusstopsFactory.create()

    actual = NowLocation.get_location(base_busstop, buses, busstops)

    assert actual == excepted
