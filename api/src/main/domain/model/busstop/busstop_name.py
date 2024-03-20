from __future__ import annotations

from pydantic import BaseModel, model_serializer


class BusstopName(BaseModel):
    """バス停名"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)

    def is_停車中(self) -> bool:
        return self.value == ""

    def __eq__(self, other):
        return self.value == other.value

    @model_serializer
    def __str__(self) -> str:
        return self.value
