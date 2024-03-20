from pydantic import BaseModel, model_serializer


class RouteNumber(BaseModel):
    """系統番号"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)

    @model_serializer
    def __str__(self) -> str:
        return self.value
