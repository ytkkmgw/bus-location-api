from api.src.test.domain.model.busstop.busstop_factory import BusstopFactory
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstops import Busstops


class BusstopsFactory:
    @staticmethod
    def create():
        busstop_factory = BusstopFactory()
        busstops: list[Busstop] = [
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Kichijoujieki.30086.3", "吉祥寺駅", 0
            ),
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Sanro-doiriguchi.30087.2", "サンロード入口", 1
            ),
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Toukyoujoshidaiiriguchi.30089.3",
                "東京女子大入口",
                2,
            ),
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Musashinodaiyonshougakkou.30090.3",
                "武蔵野第四小学校",
                3,
            ),
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Tatenochou.30091.3", "立野町", 4
            ),
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Musashinoryoumae.30092.3", "武蔵野寮前", 5
            ),
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Sekimachiminaminichoume.30093.3", "関町南二丁目", 6
            ),
            busstop_factory.create(
                "odpt.BusstopPole:SeibuBus.Toukyousanikushougakkouiriguchi.30094.3",
                "東京三育小学校入口",
                7,
            ),
        ]
        return Busstops(busstops)
