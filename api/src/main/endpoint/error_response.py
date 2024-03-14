from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse


class ErrorResponse(BaseModel):
    message: str

    def bad_request(self) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=self.model_dump(),
        )

    def not_found(self) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=self.model_dump(),
        )

    def internal_server_error(self) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=self.model_dump(),
        )
