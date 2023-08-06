import abc
from typing import Any, Mapping

from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClientSession
from pydantic.dataclasses import dataclass
from pymongo.database import Database

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
        raise TypeError('Session must be type of motor.motor_asyncio AsyncIOMotorClientSession')

    def invalid_document(self, error) -> None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=error,
        )

    def validate_session(self, session: AsyncIOMotorClientSession) -> None:
        if session is not None and not isinstance(session, AsyncIOMotorClientSession):
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
class BaseAPIView(BaseRepositoryView, abc.ABC):
    pk_field: Any = None
    statement: Mapping[str, Any] = None

    @abc.abstractmethod
    async def get_all(
            self,
            db: Database,
            session: AsyncIOMotorClientSession = None,
            limit: int = 100,
            skip: int = 0,
            **kwargs,
    ) -> list[Record]:
        """Returns multiple objects."""

    @abc.abstractmethod
    async def get_detail(
            self,
            db: Database,
            session: AsyncIOMotorClientSession = None,
            field_value: Any = None,
            **kwargs,
    ):
        """Return single object."""

    @abc.abstractmethod
    async def create(
            self,
            db: Database,
            session: AsyncIOMotorClientSession = None,
            document: Mapping[str, Any] = None,
            **kwargs,
    ):
        """Perform object creation."""

    @abc.abstractmethod
    async def delete(
            self,
            db: Database,
            field_value: Any,
            session: AsyncIOMotorClientSession = None,
            **kwargs,
    ):
        """Remove object."""

    @abc.abstractmethod
    async def update_one(
            self,
            db: Database,
            update_doc: Mapping[str, Any],
            field_value: Any = None,
            session: AsyncIOMotorClientSession = None,
            document: Mapping[str, Any] = None,
            **kwargs,
    ):
        """ Perform single object update."""
