from fastapi import Depends
from sqlalchemy.orm import exc

from domain.model.sample.comment import Comment
from domain.model.sample.mail_address import MailAddress
from domain.model.sample.user import User
from domain.model.sample.user_name import UserName
from domain.model.sample.user_number import UserNumber
from domain.policy.resource_notfound_error import ResourceNotFoundError
from engine import DBEngine
from schema.sample_shema import UserTable
from usecase.repository.sample.sample_repository import SampleRepository


class SampleDatasource(SampleRepository):
    def __init__(self, engine: DBEngine = Depends()):
        self.session = engine.create_session()

    def find(self, user_name: UserName) -> User:
        try:
            record = (
                self.session.query(UserTable)
                .filter(UserTable.user_name == user_name.value)
                .one()
            )
        except exc.NoResultFound:
            raise ResourceNotFoundError(f"レコードなし(value={user_name.value})")
        return User(
            UserNumber(record.id),
            UserName(record.user_name),
            MailAddress(record.mail),
            Comment(record.comment),
        )
