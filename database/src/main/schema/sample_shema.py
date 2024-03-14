from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserTable(Base):
    __tablename__ = "user"
    __table_args__ = {"comment": "ユーザ", "schema": "sample"}

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        comment="id",
    )
    user_name = Column(String(100), nullable=False, comment="ユーザ名")
    mail = Column(String(100), nullable=False, comment="メールアドレス")
    comment = Column(String(200), nullable=False, comment="コメント")


class User2Table(Base):
    __tablename__ = "user_2"
    __table_args__ = {"comment": "ユーザ2", "schema": "sample"}

    user_id = Column(
        Integer,
        ForeignKey("sample.user.id"),
        nullable=False,
        primary_key=True,
        comment="user_id",
    )
