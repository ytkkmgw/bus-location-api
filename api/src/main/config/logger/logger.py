import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()  # ハンドラーを作成
    handler.setLevel(logging.DEBUG)  # ハンドラーのログレベルを設定

    formatter = logging.Formatter("%(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)  # カスタムロガーにハンドラーを紐づける

    return logger
