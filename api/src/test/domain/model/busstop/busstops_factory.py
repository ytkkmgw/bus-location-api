from api.src.test.domain.model.busstop.busstop_factory import BusstopFactory
from domain.model.busstop.busstop import Busstop
from domain.model.busstop.busstops import Busstops


class BusstopsFactory:
    @staticmethod
    def create():
        busstop_factory = BusstopFactory()
        busstops: list[Busstop] = [
            busstop_factory.create("吉祥寺駅", 0),
            busstop_factory.create("サンロード入口", 1),
            busstop_factory.create("東京女子大入口", 2),
            busstop_factory.create("武蔵野第四小学校", 3),
            busstop_factory.create("立野町", 4),
            busstop_factory.create("武蔵野寮前", 5),
            busstop_factory.create("関町南二丁目", 6),
            busstop_factory.create("東京三育小学校入口", 7),
        ]
        return Busstops(busstops)
