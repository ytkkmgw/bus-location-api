from pydantic import BaseModel, model_serializer


class UserNumber(BaseModel):
    """ユーザ番号"""

    value: int

    def __init__(self, value: int):
        super().__init__(value=value)

    @model_serializer
    def __int__(self) -> int:
        return self.value
