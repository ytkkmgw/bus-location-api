from pydantic import BaseModel


class BusstopPlatform(BaseModel):
    """のりば番号"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)
