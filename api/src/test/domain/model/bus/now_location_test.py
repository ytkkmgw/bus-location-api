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


class TestNowLocation:
    """現在位置テストケース"""

    buses: Buses = Buses(
        [
            Bus(
                BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
                DepartureTime("17:30"),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Sanro-doiriguchi.30087.2", "サンロード入口", 1
                ),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Toukyoujoshidaiiriguchi.30089.3",
                    "東京女子大入口",
                    2,
                ),
            ),
            Bus(
                BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
                DepartureTime("17:00"),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Musashinoryoumae.30092.3", "武蔵野寮前", 5
                ),
                BusstopFactory.create_empty(),
            ),
        ]
    )

    @pytest.mark.parametrize(
        "busstop_identifier,busstop_name, busstop_number, excepted",
        [
            (
                "odpt.BusstopPole:SeibuBus.Kichijoujieki.30086.3",
                "吉祥寺駅",
                0,
                NowLocation.NONE,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Sanro-doiriguchi.30087.2",
                "サンロード入口",
                1,
                NowLocation.NONE,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Toukyoujoshidaiiriguchi.30089.3",
                "東京女子大入口",
                2,
                NowLocation.SOON,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Musashinodaiyonshougakkou.30090.3",
                "武蔵野第四小学校",
                3,
                NowLocation.ONE_TWO,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Tatenochou.30091.3",
                "立野町",
                4,
                NowLocation.TWO_THREE,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Musashinoryoumae.30092.3",
                "武蔵野寮前",
                5,
                NowLocation.NOW,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Sekimachiminaminichoume.30093.3",
                "関町南二丁目",
                6,
                NowLocation.ONE,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Toukyousanikushougakkouiriguchi.30094.3",
                "東京三育小学校入口",
                7,
                NowLocation.TWO,
            ),
        ],
    )
    def test_get_location(
        self, busstop_identifier, busstop_name, busstop_number, excepted
    ):
        """バス停一覧・バス便一覧から現在位置を取得できる"""
        base_busstop: Busstop = BusstopFactory.create(
            busstop_identifier, busstop_name, busstop_number
        )
        busstops: Busstops = BusstopsFactory.create()
        recent_bus: Bus = self.buses.recent_bus(base_busstop)
        actual = NowLocation.get_location(recent_bus, base_busstop)

        assert actual == excepted
