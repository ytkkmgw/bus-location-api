from abc import abstractmethod, ABC

from domain.model.sample.user import User
from domain.model.sample.user_name import UserName


class SampleRepository(ABC):
    @abstractmethod
    def find(self, user_name: UserName) -> User:
        pass
