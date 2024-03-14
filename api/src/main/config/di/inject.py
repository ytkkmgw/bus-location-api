from domain.policy.unsupported_operation_error import UnsupportedOperationError

# injectする際にimportが必要な為、グレーアウトしているがimportは残している。
from infrastructure.datasource.sample.sample_datasource import *


def inject(obj):
    sub_classe = obj.__subclasses__()
    if len(sub_classe) < 1:
        raise NotImplementedError("Repositoryに実装クラスがありません")
    if len(sub_classe) > 1:
        raise UnsupportedOperationError("実装クラスが複数あります。")
    return sub_classe[0]
