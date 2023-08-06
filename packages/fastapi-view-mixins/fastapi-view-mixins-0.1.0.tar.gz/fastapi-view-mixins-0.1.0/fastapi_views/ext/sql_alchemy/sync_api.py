from typing import Any, Generic, TypeVar

from fastapi import status
from fastapi.responses import Response
from pydantic.dataclasses import dataclass
from sqlalchemy import delete, func, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

from fastapi_views.ext.sql_alchemy.core import BaseAPIView
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record

Table = TypeVar("Table")


@dataclass(config=BaseConfig)
class SyncAPI(BaseAPIView, Generic[Table]):
    """Sync API with default methods to get, create, update, delete objects."""

    @staticmethod
    def _count(session: Session, statement: Select) -> int:
        """Get number of documents for given statement."""
        count_statement = select(func.count()).select_from(statement.subquery())
        return session.scalar(count_statement)

    def get_all(
            self,
            session: Session,
            limit: int = 100,
            offset: int = 0,
            **kwargs,
    ) -> list[Record]:
        self.validate_session(session)
        self.validate_statement()
        return session.execute(self.statement.limit(limit).offset(limit * offset), **kwargs).all()

    def get_detail(self, session: Session, field_value: Any = None, **kwargs) -> Table:
        """Fetch object."""
        self.validate_session(session)

        if self.statement is not None:
            statement = self.statement
        else:
            self.validate_field_value(field_value)
            statement = select(self.model).where(getattr(self.model, self.pk_field) == field_value)

        if self._count(session, statement) > 1:
            raise ValueError('Multiple objects returned')
        result = session.scalar(statement, **kwargs)

        if result is None:
            self.exceptions.not_found_exception(field_value)
        return result

    def create(self, session: Session, data: dict[str, Any] = None) -> Table:
        """Create object."""
        self.validate_session(session)
        if data is None:
            data = {}
        entry = self.model(**data)
        try:
            session.add(entry)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            self.exceptions.integrity_error(str(e.orig))

        session.refresh(entry)
        return entry

    def delete(self, session: Session, field_value: Any, **kwargs) -> Response:
        """Remove object."""
        if self.pk_field is None:
            self.exceptions.attribute_error('pk_field')
        self.validate_session(session)
        self.validate_field_value(field_value)

        statement = delete(self.model).where(getattr(self.model, self.pk_field) == field_value)
        session.execute(statement, **kwargs)
        session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    def update_one(
            self,
            session: Session,
            field_value: Any,
            data: dict[str, Any] = None,
            synchronize_session='fetch',
            **kwargs,
    ) -> None:
        """Update object."""
        self.validate_session(session)
        self.validate_field_value(field_value)
        if self.pk_field is None:
            self.exceptions.attribute_error('pk_field')
        if data is None or not data:
            self.exceptions.empty_update_error()

        statement = update(self.model) \
            .where(getattr(self.model, self.pk_field) == field_value) \
            .values(**data) \
            .execution_options(synchronize_session=synchronize_session)
        try:
            session.execute(statement, **kwargs)
        except IntegrityError as e:
            session.rollback()
            self.exceptions.integrity_error(str(e.orig))
        else:
            session.commit()
