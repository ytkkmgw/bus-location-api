from fastapi import Depends

from config.di.inject import inject
from domain.model.sample.user import User
from domain.model.sample.user_name import UserName
from usecase.repository.sample.sample_repository import SampleRepository


class SampleService:
    def __init__(
        self, sample_repository: SampleRepository = Depends(inject(SampleRepository))
    ):
        self.sample_repository = sample_repository

    def find(self, user_name: UserName) -> User:
        return self.sample_repository.find(user_name)
