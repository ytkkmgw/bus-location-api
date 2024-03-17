from pydantic import BaseModel

from domain.model.route.bus_route import BusRoute


class BusRoutes(BaseModel):
    """バス運行系統一覧"""

    routes: list[BusRoute]

    def __init__(self, routes: list[BusRoute]):
        super().__init__(routes=routes)
