from pydantic import BaseModel

from domain.model.route.route_identifier import RouteIdentifier


class RouteIdentifiers(BaseModel):
    """運行系統識別子一覧"""

    identifiers: list[RouteIdentifier]

    def __init__(self, route_identifiers: list[RouteIdentifier]):
        super().__init__(identifiers=route_identifiers)

    def as_str_list(self):
        result=[]
        for identifier in self.identifiers:
            result.append(identifier.value)
        return result
