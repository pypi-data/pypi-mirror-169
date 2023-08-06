import abc
# from api.base import BaseAPI
from typing import Any, Union

from fastapi.requests import Request
from pydantic.dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

from fastapi_views.ext.sql_alchemy.pagination.core import paginate_api
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record
from fastapi_views.views.core import BaseRepositoryView, RepositoryExceptions


class APIErrorHandlers:
    exceptions: RepositoryExceptions
    statement: Select

    def statement_type_error(self) -> None:
        raise TypeError('Statement must be type of sqlalchemy.sql Select')

    def session_type_error(self) -> None:
        raise TypeError('Session must be type of sqlalchemy.orm Session')

    def async_session_type_error(self) -> None:
        raise TypeError('Session must be type of sqlalchemy.ext.asyncio AsyncSession')

    def validate_session(self, session: Session) -> None:
        if session is None:
            self.exceptions.attribute_error('session')
        if not isinstance(session, Session):
            self.session_type_error()

    def validate_async_session(self, session: AsyncSession) -> None:
        if session is None:
            self.exceptions.attribute_error('session')
        if not isinstance(session, AsyncSession):
            self.async_session_type_error()

    def validate_statement(self) -> None:
        if self.statement is None:
            self.exceptions.attribute_error('statement')
        if not isinstance(self.statement, Select):
            self.statement_type_error()

    def validate_field_value(self, unique: Any) -> None:
        if unique is None:
            self.exceptions.attribute_error('pk')


@dataclass(config=BaseConfig)
class BaseAPIView(BaseRepositoryView, APIErrorHandlers, abc.ABC):
    pk_field: Any = None
    statement: Select = None

    def get_all_with_pagination(self, request: Request, session: Session):
        """Returns multiple objects using pagination."""
        self.validate_session(session)
        self.validate_pagination(request)

        paginate_response = paginate_api(
            statement=self.statement,
            request=request,
            session=session,
            paginate_by=self.paginate_by,
            strategy=self.pagination_strategy,
            kwargs=self.pagination_kwargs,
        )
        return paginate_response

    @abc.abstractmethod
    def get_all(
            self,
            session: Union[Session, AsyncSession],
            limit: int = 100,
            offset: int = 0,
            **kwargs,
    ) -> list[Record]:
        """Returns multiple objects."""

    @abc.abstractmethod
    def get_detail(self, session: Union[Session, AsyncSession], field_value: Any, **kwargs):
        """Return single object."""

    @abc.abstractmethod
    def create(self, session: Union[Session, AsyncSession], data: dict[str, Any]):
        """Perform object creation."""

    @abc.abstractmethod
    def delete(self, session: Union[Session, AsyncSession], field_value: Any, **kwargs):
        """Remove object."""

    @abc.abstractmethod
    def update_one(
            self,
            session: Union[Session, AsyncSession],
            field_value: Any,
            data: dict[str, Any],
            synchronize_session='fetch',
            **kwargs,
    ):
        """
        Perform single object update.

        synchronize_session: check sqlalchemy doc for details.
        """
