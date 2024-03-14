import os


def docs_path():
    if os.environ["ENV_NAME"] == "prod":
        return None
    return "/docs"


def redoc_path():
    if os.environ["ENV_NAME"] == "prod":
        return None
    return "/redoc"
