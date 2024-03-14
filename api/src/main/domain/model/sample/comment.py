from pydantic import BaseModel, model_serializer


class Comment(BaseModel):
    """コメント"""

    value: str

    def __init__(self, value: str):
        super().__init__(value=value)

    @model_serializer
    def __str__(self) -> str:
        return self.value
