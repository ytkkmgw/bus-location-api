import pytest
from api.src.test.domain.model.busstop.busstop_factory import BusstopFactory
from api.src.test.domain.model.busstop.busstops_factory import BusstopsFactory
from domain.model.bus.bus import Bus
from domain.model.bus.bus_identifier import BusIdentifier
from domain.model.bus.buses import Buses
from domain.model.bus.departure_time import DepartureTime
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstops import Busstops


class TestBuses:
    """バス便一覧テストケース"""

    buses: Buses = Buses(
        [
            Bus(
                BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
                DepartureTime("17:30"),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Toukyoujoshidaiiriguchi.30089.3",
                    "東京女子大",
                    2,
                ),
                BusstopFactory.create_empty(),
            ),
            Bus(
                BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
                DepartureTime("17:15"),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Musashinodaiyonshougakkou.30090.3",
                    "武蔵野第四小学校",
                    3,
                ),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Tatenochou.30091.3", "立野町", 4
                ),
            ),
            Bus(
                BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
                DepartureTime("17:00"),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Sekimachiminaminichoume.30093.3",
                    "関町南二丁目",
                    6,
                ),
                BusstopFactory.create_empty(),
            ),
            Bus(
                BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.670"),
                DepartureTime("16:45"),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Sekimachiminaminichoume.30093.3",
                    "関町南二丁目",
                    6,
                ),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Toukyousanikushougakkouiriguchi.30094.3",
                    "東京三育小学校入口",
                    7,
                ),
            ),
            Bus(
                BusIdentifier("odpt.Bus:SeibuBus.Yoshi60.52001.1.669"),
                DepartureTime("16:30"),
                BusstopFactory.create(
                    "odpt.BusstopPole:SeibuBus.Toukyousanikushougakkouiriguchi.30094.3",
                    "東京三育小学校入口",
                    7,
                ),
                BusstopFactory.create_empty(),
            ),
        ]
    )

    @pytest.mark.parametrize(
        "busstop_identifier,busstop_name, busstop_number, result_index",
        [
            (
                "odpt.BusstopPole:SeibuBus.Toukyoujoshidaiiriguchi.30089.3",
                "東京女子大",
                2,
                0,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Musashinodaiyonshougakkou.30090.3",
                "武蔵野第四小学校",
                3,
                0,
            ),
            ("odpt.BusstopPole:SeibuBus.Tatenochou.30091.3", "立野町", 4, 1),
            (
                "odpt.BusstopPole:SeibuBus.Sekimachiminaminichoume.30093.3",
                "関町南二丁目",
                6,
                2,
            ),
            (
                "odpt.BusstopPole:SeibuBus.Toukyousanikushougakkouiriguchi.30094.3",
                "東京三育小学校入口",
                7,
                4,
            ),
        ],
    )
    def test_recent_bus(
        self, busstop_identifier, busstop_name, busstop_number, result_index
    ):
        """直近のバス便を取得できる"""

        base_busstop: Busstop = BusstopFactory.create(
            busstop_identifier, busstop_name, busstop_number
        )

        actual = self.buses.recent_bus(base_busstop)

        assert self.buses.as_list()[result_index] == actual

    @pytest.mark.parametrize(
        "busstop_identifier,busstop_name, busstop_number",
        [
            ("odpt.BusstopPole:SeibuBus.Kichijoujieki.30086.3", "吉祥寺駅", 0),
            ("odpt.BusstopPole:SeibuBus.Sanro-doiriguchi.30087.2", "サンロード入口", 1),
        ],
    )
    def test_no_recent_bus(self, busstop_identifier, busstop_name, busstop_number):
        """直近のバス便が無い場合または始発バス停の場合はNoneが返る"""
        base_busstop: Busstop = BusstopFactory.create(
            busstop_identifier, busstop_name, busstop_number
        )

        actual = self.buses.recent_bus(base_busstop)

        assert actual is None
