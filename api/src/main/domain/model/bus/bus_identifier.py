from pydantic import BaseModel


class BusIdentifier(BaseModel):
    """バス便識別子"""

    value: str

    def __init__(self, value: str):
        if value is None:
            super().__init__(value="")
            return
        super().__init__(value=value)

    def is_empty(self) -> bool:
        return self.value == ""
