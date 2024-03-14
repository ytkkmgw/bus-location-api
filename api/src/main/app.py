from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from config.openapi.doc_path import docs_path, redoc_path
from endpoint.exception_handlers import exception_handlers
from endpoint.sample import sample_controller


app = FastAPI(
    title="fastapi-template",
    servers=[
        {"url": "http://localhost:8080", "description": "ローカル"},
        {"url": "http://localhost:18080", "description": "ローカル(コンテナ)"},
        {"url": "https://y-fastapi-template.fly.dev", "description": "本番"},
    ],
    docs_url=docs_path(),
    redoc_url=redoc_path(),
)

# 422エラーは返さない為、docsから422エラーを削除する。
def custom_openapi():
    if not app.openapi_schema:
        app.openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for _, method_item in app.openapi_schema.get("paths").items():
            for _, param in method_item.items():
                responses = param.get("responses")
                # remove 422 response, also can remove other status code
                if "422" in responses:
                    del responses["422"]
    return app.openapi_schema


app.openapi = custom_openapi

exception_handlers(app)

# 以下にcontrollerのrouterを定義する
app.include_router(sample_controller.router)
