import abc
from typing import Any, Mapping

from fastapi import HTTPException, status
from fastapi.requests import Request
from pydantic.dataclasses import dataclass
from pymongo.client_session import ClientSession
from pymongo.database import Database

from fastapi_views.ext.pymongo.pagination.core import paginate_api
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record
from fastapi_views.views.core import BaseRepositoryView, RepositoryExceptions


class APIErrorHandlers:
    exceptions: RepositoryExceptions
    statement: Mapping[str, Any]
    model: str

    def statement_type_error(self) -> None:
        raise TypeError('Statement must be type of dict')

    def session_type_error(self) -> None:
        raise TypeError('Session must be type of pymongo ClientSession')

    def invalid_document(self, error) -> None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=error,
        )

    def validate_session(self, session: ClientSession) -> None:
        if session is not None and not isinstance(session, ClientSession):
            self.session_type_error()

    def validate_statement(self) -> None:
        if self.statement is None:
            self.exceptions.attribute_error('statement')
        if not isinstance(self.statement, dict):
            self.statement_type_error()

    def validate_field_value(self, unique: Any) -> None:
        if unique is None:
            self.exceptions.attribute_error('pk')

    def not_found_exception(self, unique: Any):
        """Object not found exception."""
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{self.model} with <{type(unique)}:{unique}> does not exists.'
        )


@dataclass(config=BaseConfig)
class BaseAPIView(BaseRepositoryView, APIErrorHandlers, abc.ABC):
    """
    Arguments:
        ** model ** : mongodb collection name
    """
    pk_field: Any = None
    statement: Mapping[str, Any] = None

    def get_all_with_pagination(
            self,
            db: Database,
            request: Request,
            session: ClientSession = None,
            **kwargs,
    ):
        """Returns multiple objects using pagination."""
        self.validate_session(session)
        self.validate_pagination(request)
        self.pagination_kwargs['collection'] = getattr(db, self.model)

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
            db: Database,
            session: ClientSession = None,
            limit: int = 100,
            skip: int = 0,
            **kwargs) -> list[Record]:
        """Returns multiple objects."""

    @abc.abstractmethod
    def get_detail(
            self,
            db: Database,
            session: ClientSession = None,
            field_value: Any = None,
            **kwargs,
    ):
        """Return single object."""

    @abc.abstractmethod
    def create(
            self,
            db: Database,
            document: Mapping[str, Any],
            session: ClientSession = None,
            **kwargs,
    ):
        """Perform object creation."""

    @abc.abstractmethod
    def delete(
            self,
            db: Database,
            field_value: Any,
            session: ClientSession = None,
            **kwargs,
    ):
        """Remove object."""

    @abc.abstractmethod
    def update_one(
            self,
            db: Database,
            update_doc: Mapping[str, Any],
            field_value: Any = None,
            session: ClientSession = None,
            document: Mapping[str, Any] = None,
            **kwargs,
    ):
        """ Perform single object update."""
