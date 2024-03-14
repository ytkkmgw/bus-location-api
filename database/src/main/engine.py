import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session


class DBEngine:
    def __init__(self):
        url = os.environ["DATABASE_URL"]
        self.engine: Engine = create_engine(url, echo=True)

    def create_session(self) -> Session:
        return Session(autocommit=False, autoflush=True, bind=self.engine)
