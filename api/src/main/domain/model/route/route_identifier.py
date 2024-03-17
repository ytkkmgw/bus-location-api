from pydantic import BaseModel


class RouteIdentifier(BaseModel):
    """運行系統識別子"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)
