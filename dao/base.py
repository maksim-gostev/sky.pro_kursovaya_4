from typing import Generic, Optional, TypeVar
from sqlalchemy.orm import scoped_session

from dao.model.models_main import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):

    __model__ = Base

    def __init__(self, session: scoped_session) -> None:
        self.session = session

    def get_by_id(self, pk: int) -> Optional[T]:
        return self.session.query(self.__model__).get(pk)
