from injector import Injector

from infrastructure.datasource.bus.bus_datasource import BusDataSource
from infrastructure.datasource.pole.pole_datasource import PoleDatasource
from infrastructure.datasource.route.route_datasource import RouteDatasource
from usecase.repository.bus.bus_repository import BusRepository
from usecase.repository.pole.pole_repository import PoleRepository
from usecase.repository.route.route_repository import RouteRepository


class Dependency:
    def __init__(self) -> None:
        # 依存関係を設定する関数を読み込む
        self.injector = Injector(self.__class__.config)

    # 依存関係を設定するメソッド
    @classmethod
    def config(cls, binder):
        # 抽象クラスをインスタンス化する際にCatクラスを使うよう登録する
        binder.bind(PoleRepository, PoleDatasource)
        binder.bind(BusRepository, BusDataSource)
        binder.bind(RouteRepository, RouteDatasource)

    # injector.get()に引数を渡すと依存関係を解決してインスタンスを生成する
    @staticmethod
    def get(cls):
        return Dependency().injector.get(cls)
