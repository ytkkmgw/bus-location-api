from pydantic import BaseModel, model_serializer


class BusstopPoleNumber(BaseModel):
    """バス停標柱番号"""

    value: int

    def __init__(self, value: int):
        super().__init__(value=value)

    @model_serializer
    def __int__(self) -> int:
        return self.value
