import fastapi
import os
from fastapi import Depends
from starlette import status

from domain.model.sample.user import User
from domain.model.sample.user_name import UserName
from endpoint.error_response import ErrorResponse
from usecase.service.sample.sample_service import SampleService

router = fastapi.APIRouter(prefix="/sample", tags=["サンプル"])


@router.get(
    "/",
    summary="サンプルエンドポイント1",
    description="固定値を返すサンプルエンドポイント",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "その他サーバに起因するエラーにより処理続行できない",
            "model": ErrorResponse,
        },
    },
)
async def root():
    return {"message": "Hello World"}


@router.get(
    "/user",
    summary="サンプルエンドポイント2",
    description="URLに入力した値を返すサンプルエンドポイント",
    response_model=User,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "パラメータ不正", "model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"description": "レコードなし", "model": ErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "その他サーバに起因するエラーにより処理続行できない",
            "model": ErrorResponse,
        },
    },
)
async def say_hello(name: str, sample_service: SampleService = Depends()):
    return sample_service.find(UserName(name))


@router.get(
    "/env",
    summary="環境変数エンドポイント",
    description="設定中の環境変数を返すエンドポイント",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "その他サーバに起因するエラーにより処理続行できない",
            "model": ErrorResponse,
        },
    },
)
async def get_env():
    return {
        "ENV_NAME": os.environ.get("ENV_NAME"),
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
    }
