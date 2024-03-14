from typing import Union

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from config.logger.logger import get_logger
from domain.policy.resource_notfound_error import ResourceNotFoundError
from endpoint.error_response import ErrorResponse

log = get_logger("exception_handlers")


def exception_handlers(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    @app.exception_handler(ValidationError)
    def validation_error_handler(
        request, exception: Union[RequestValidationError, ValidationError]
    ):
        return ErrorResponse(message="不正パラメータ").bad_request()

    @app.exception_handler(ResourceNotFoundError)
    def validation_error_handler(request, exception: ResourceNotFoundError):
        return ErrorResponse(message="該当レコードなし").not_found()

    @app.exception_handler(Exception)
    def exception_handler(request, exception):
        log.error(exception)
        return ErrorResponse(message="サーバ内で予期せぬエラーが発生しました").internal_server_error()
