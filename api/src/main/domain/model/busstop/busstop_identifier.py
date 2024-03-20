from __future__ import annotations

from pydantic import BaseModel


class BusstopIdentifier(BaseModel):
    """バス停識別子"""

    value: str

    def __init__(self, value: str):
        if value is None:
            super().__init__(value="バス停識別子なし")
            return
        super().__init__(value=value)

    def __eq__(self, other: BusstopIdentifier) -> bool:
        return self.value == other.value
