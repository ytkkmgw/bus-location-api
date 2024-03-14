from pydantic import BaseModel

from domain.model.sample.comment import Comment
from domain.model.sample.mail_address import MailAddress
from domain.model.sample.user_name import UserName
from domain.model.sample.user_number import UserNumber


class User(BaseModel):
    """ユーザー"""

    number: UserNumber
    name: UserName
    mail_address: MailAddress
    comment: Comment

    def __init__(
        self,
        number: UserNumber,
        name: UserName,
        mail_address: MailAddress,
        comment: Comment,
    ):
        super().__init__(
            number=number, name=name, mail_address=mail_address, comment=comment
        )
