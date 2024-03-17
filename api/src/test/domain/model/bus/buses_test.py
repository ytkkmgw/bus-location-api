"""バス便一覧テストケース"""
import pytest

from api.src.test.domain.model.busstop.busstop_factory import BusstopFactory
from api.src.test.domain.model.busstop.busstops_factory import BusstopsFactory
from domain.model.bus.bus import Bus
from domain.model.bus.bus_identifier import BusIdentifier
from domain.model.bus.buses import Buses
from domain.model.bus.departure_time import DepartureTime
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstops import Busstops


buses: Buses = Buses(
    [
        Bus(
            BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
            DepartureTime("16:57"),
            BusstopFactory.create("東京女子大", 2),
            BusstopFactory.empty_create(),
        ),
        Bus(
            BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
            DepartureTime("16:57"),
            BusstopFactory.create("武蔵野第四小学校", 3),
            BusstopFactory.create("立野町", 4),
        ),
        Bus(
            BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
            DepartureTime("16:56"),
            BusstopFactory.create("関町南二丁目", 6),
            BusstopFactory.empty_create(),
        ),
        Bus(
            BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
            DepartureTime("16:55"),
            BusstopFactory.create("関町南二丁目", 6),
            BusstopFactory.create("東京三育小学校入口", 7),
        ),
        Bus(
            BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.669"),
            DepartureTime("16:50"),
            BusstopFactory.create("東京三育小学校入口", 7),
            BusstopFactory.empty_create(),
        ),
    ]
)


@pytest.mark.parametrize(
    "busstop_name, busstop_number, result_index",
    [
        ("東京女子大", 2, 0),
        ("武蔵野第四小学校", 3, 0),
        ("立野町", 4, 1),
        ("関町南二丁目", 6, 2),
        ("東京三育小学校入口", 7, 4),
    ],
)
def test_recent_bus(busstop_name, busstop_number, result_index):
    """直近のバス便を取得できる"""

    base_busstop: Busstop = BusstopFactory.create(busstop_name, busstop_number)
    busstops: Busstops = BusstopsFactory.create()

    actual = buses.recent_bus(base_busstop, busstops)

    assert buses.as_list()[result_index] == actual


@pytest.mark.parametrize(
    "busstop_name, busstop_number",
    [
        ("吉祥寺駅", 0),
        ("サンロード入口", 1),
    ],
)
def test_no_recent_bus(busstop_name, busstop_number):
    """直近のバス便が無い場合または始発バス停の場合はNoneが返る"""
    base_busstop: Busstop = BusstopFactory.create(busstop_name, busstop_number)
    busstops: Busstops = BusstopsFactory.create()

    actual = buses.recent_bus(base_busstop, busstops)

    assert actual is None