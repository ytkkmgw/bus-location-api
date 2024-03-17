from pydantic import BaseModel


class RouteNumber(BaseModel):
    """系統番号"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)
