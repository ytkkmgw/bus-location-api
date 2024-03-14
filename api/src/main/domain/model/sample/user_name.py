from pydantic import BaseModel, model_serializer, Field


class UserName(BaseModel):
    """ユーザー名"""

    value: str = Field(min_length=1)

    def __init__(self, value: str):
        super().__init__(value=value)

    @model_serializer
    def __str__(self) -> str:
        return self.value
