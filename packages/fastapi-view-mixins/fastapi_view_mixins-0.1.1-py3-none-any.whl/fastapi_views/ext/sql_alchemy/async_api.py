from typing import Any, Generic, TypeVar

from fastapi import status
from fastapi.requests import Request
from fastapi.responses import Response
from pydantic.dataclasses import dataclass
from sqlalchemy import delete, func, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select

from fastapi_views.ext.sql_alchemy.core import BaseAPIView
from fastapi_views.ext.sql_alchemy.pagination.core import async_paginate_api
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record

Table = TypeVar("Table")


@dataclass(config=BaseConfig)
class AsyncAPI(BaseAPIView, Generic[Table]):
    """Async API with default methods to get, create, update, delete objects."""

    @staticmethod
    async def _count(session: AsyncSession, statement: Select) -> int:
        """Get number of documents for given statement."""
        count_statement = select(func.count()).select_from(statement.subquery())
        return await session.scalar(count_statement)

    async def get_all(
            self, session: AsyncSession,
            limit: int = 100,
            offset: int = 0,
            **kwargs,
    ) -> list[Record]:
        """Fetch all objects."""
        self.validate_async_session(session)
        self.validate_statement()
        return (await session.execute(
            self.statement.limit(limit).offset(limit * offset),
            **kwargs
        )).all()

    async def get_all_with_pagination(self, request: Request, session: AsyncSession):
        """Returns pagination object."""
        self.validate_async_session(session)
        self.validate_pagination(request)
        paginate_response = await async_paginate_api(
            statement=self.statement,
            request=request,
            session=session,
            paginate_by=self.paginate_by,
            strategy=self.pagination_strategy,
            kwargs=self.pagination_kwargs,
        )
        return paginate_response

    async def get_detail(self, session: AsyncSession, field_value: Any = None, **kwargs) -> Table:
        """Fetch object."""
        self.validate_async_session(session)

        if self.statement is not None:
            statement = self.statement
        else:
            self.validate_field_value(field_value)
            statement = select(self.model).where(getattr(self.model, self.pk_field) == field_value)

        if await self._count(session, statement) > 1:
            raise ValueError('Multiple objects returned')
        result = await session.scalar(statement, **kwargs)

        if result is None:
            self.exceptions.not_found_exception(field_value)
        return result

    async def create(self, session: AsyncSession, data: dict[str, Any] = None) -> Table:
        """Create object."""
        self.validate_async_session(session)
        if data is None:
            data = {}
        entry = self.model(**data)
        try:
            session.add(entry)
            await session.commit()
        except IntegrityError as e:
            await session.rollback()
            self.exceptions.integrity_error(str(e.orig))

        await session.refresh(entry)
        return entry

    async def delete(self, session: AsyncSession, field_value: Any, **kwargs) -> Response:
        """Remove object."""
        if self.pk_field is None:
            self.exceptions.attribute_error('pk_field')
        self.validate_async_session(session)
        self.validate_field_value(field_value)

        statement = delete(self.model).where(getattr(self.model, self.pk_field) == field_value)
        await session.execute(statement, **kwargs)
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    async def update_one(
            self,
            session: AsyncSession,
            field_value: Any,
            data: dict[str, Any] = None,
            synchronize_session='fetch',
            **kwargs,
    ) -> None:
        """Update object."""
        self.validate_async_session(session)
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
            await session.execute(statement, **kwargs)
        except IntegrityError as e:
            await session.rollback()
            self.exceptions.integrity_error(str(e.orig))
        else:
            await session.commit()
