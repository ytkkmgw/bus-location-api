from pydantic import BaseModel


class Destination(BaseModel):
    """行先"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)
