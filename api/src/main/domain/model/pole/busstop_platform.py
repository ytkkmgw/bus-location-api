from pydantic import BaseModel, model_serializer


class BusstopPlatform(BaseModel):
    """のりば番号"""

    value: str

    def __init__(self, value: str):
        if value is None:
            super().__init__(value="のりば番号設定なし")
            return
        super().__init__(value=value)

    @model_serializer
    def __str__(self) -> str:
        return self.value
