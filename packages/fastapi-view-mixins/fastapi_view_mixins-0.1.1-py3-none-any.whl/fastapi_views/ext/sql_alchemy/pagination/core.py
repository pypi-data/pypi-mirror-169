import operator
from functools import cached_property
from typing import Any, Type, Union

from fastapi.requests import Request
from pydantic.dataclasses import dataclass
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute, Session
from sqlalchemy.sql import Select

from fastapi_views.pagination.annotations import (
    CursorResponse,
    LimitOffsetResponse,
    PaginationKwargs
)
from fastapi_views.pagination.core import (
    BasePaginationCursor,
    BasePaginationLimitOffset,
    BasePaginatorAPI,
    PaginationBase
)
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record
from fastapi_views.utils import get_regex_group


class PaginationCursor(BasePaginationCursor):
    """Cursor pagination."""

    session: Session
    statement: Select

    def _filter_query(self) -> Union[Select, None]:
        decoded_cursor = self.decoded_cursor
        is_next_page = decoded_cursor.startswith(self.next_prefix)
        prefix, op = self._get_prefix_and_operator(is_next_page)

        python_operator = getattr(operator, op)
        regex_result = get_regex_group(f'(?<={prefix})(.*)(?=&page__)', decoded_cursor)
        try:
            regex_result = int(regex_result)
        except ValueError:
            ...
        return self.statement.where(
            python_operator(
                getattr(self.model, self.get_first_order_field()),
                regex_result,
            )
        )

    def _validate_first_ordering_field(self) -> None:
        ordering = self.kwargs.get('ordering')
        first_order = ordering[0]
        first_model_field = self._get_ordering_model_field(
            first_order
        )
        if str(first_model_field.type) in ('BOOLEAN',):
            raise TypeError(f'{first_model_field.type} should can not be used as comparison')

    def _create_model_ordering(self) -> None:
        self._validate_first_ordering_field()
        result = []

        for f_name in self.kwargs.get('ordering'):
            model_field = self._get_ordering_model_field(f_name)

            if self.is_ordering_model_field_negative(f_name):
                model_field = model_field.desc()
            result.append(model_field)
        self.model_ordering = result

    def _get_ordering_model_field(self, f_name: str) -> InstrumentedAttribute:
        model = self.kwargs['model']
        if self.is_ordering_model_field_negative(f_name):
            regex_result = get_regex_group('(?<=-).*', f_name)
            return getattr(model, regex_result)

        return getattr(model, f_name)

    def _get_query_result(self) -> list[Record]:
        statement = self.statement if self.cursor is None else self._filter_query()
        return (self.session.scalars(
            statement.order_by(
                *self.model_ordering,
            ).limit(self.limit + 1))
        ).all()

    def paginate_object_list(
            self,
            request,
            *args,
            **kwargs: PaginationKwargs,
    ) -> list[Record]:
        self.session, self.statement = args
        return super().paginate_object_list(request, **kwargs)

    def get_paginated_response(self, object_list) -> CursorResponse:
        return {
            'results': object_list,
            'count': self.count,
            'page_limit': self.limit,
            'first_page': self._get_first_url(),
            'next_page': self._build_uri(self._get_next_url()),
            'previous_page': self._build_uri(self._get_previous_url()),
        }


class PaginationLimitOffset(BasePaginationLimitOffset):
    """Limit offset pagination."""

    session: Session
    statement: Select

    def _get_objects(self) -> list[Record]:
        return (self.session.execute(
            self.statement.limit(self.limit).offset(self.limit * self.page),
        )).all()

    @cached_property
    def count(self) -> int:
        statement = select(func.count()).select_from(self.statement.subquery())
        return self.session.scalar(statement)

    def paginate_object_list(
            self,
            request: Request,
            *args,
            **kwargs,
    ) -> list[Record]:
        self.session, self.statement = args
        return super().paginate_object_list(request)


@dataclass(config=BaseConfig)
class PaginatorAPI(BasePaginatorAPI):
    """
    Paginator API.

    Arguments:
        ** statement **: sqlalchemy selectable select.
        ** session **: sqlalchemy orm sync session.
    """
    statement: Select = None
    session: Session = None

    def __post_init__(self):
        if self.strategy is None:
            self.strategy = PaginationLimitOffset
        super().__post_init__()

    @property
    def _strategy_data(self) -> list[Any]:
        """Returns only list of current page objects data."""
        return self.strategy_instance.paginate_object_list(
            self.request,
            self.session,
            self.statement,
            **self.kwargs,
        )


def paginate_api(
        statement: Select,
        request: Request,
        session: Session,
        paginate_by: int = 100,
        strategy: Type[PaginationBase] = None,
        kwargs: Union[dict[str, Any], None] = None,
):
    """
    Returns pagination object for given strategy.

    :param statement: sqlalchemy selectable select
    :param request: fastapi Request object.
    :param session: session object
    :param paginate_by: number of objects per page
    :param strategy: pagination strategy object
    :param kwargs: optional params passed to strategy'/s paginate_object_list method
    """
    paginator = PaginatorAPI(
        statement=statement,
        request=request,
        session=session,
        strategy=strategy,
        paginate_by=paginate_by,
        kwargs=kwargs,
    )
    return paginator.strategy_response()


# ----- ASYNC -----

@dataclass(config=BaseConfig)
class AsyncPaginatorAPI(BasePaginatorAPI):
    """Async paginator ext."""
    statement: Select = None
    session: AsyncSession = None

    def __post_init__(self):
        if self.strategy is None:
            self.strategy = AsyncPaginationLimitOffset
        super().__post_init__()

    @property
    async def _strategy_data(self) -> list[Any]:
        """Returns only list of current page objects data."""
        return await self.strategy_instance.paginate_object_list(
            self.request,
            self.session,
            self.statement,
            **self.kwargs,
        )

    async def strategy_response(self) -> dict[str, Any]:
        """Create and return response."""
        return await self.strategy_instance.get_paginated_response(await self._strategy_data)


class AsyncPaginationLimitOffset(BasePaginationLimitOffset):
    """Pagination limit offset async extension."""

    session: AsyncSession
    statement: Select
    _count: int = None

    async def _get_objects(self) -> list[Record]:
        return (await self.session.execute(
            self.statement.limit(self.limit).offset(self.limit * self.page),
        )).all()

    @cached_property
    async def count(self) -> int:
        statement = select(func.count()).select_from(self.statement.subquery())
        return await self.session.scalar(statement)

    async def paginate_object_list(
            self,
            request: Request,
            *args,
            **kwargs,
    ) -> list[Record]:
        self.session, self.statement = args
        self.request = request
        self.paginate_by = request.state.paginate_by
        self._count = await self.count

        self.page = self._get_page(request.query_params)
        self.limit = self._get_limit(request.query_params)

        return await self._get_objects()

    async def get_paginated_response(self, object_list: list[Record]) -> LimitOffsetResponse:
        return super().get_paginated_response(object_list)


class AsyncPaginationCursor(PaginationCursor):
    """Async paginator cursors extension."""

    session: AsyncSession
    statement: Select
    _objects = None

    async def _get_query_result(self) -> list[Record]:
        statement = self.statement if self.cursor is None else self._filter_query()
        return (await self.session.scalars(
            statement.order_by(
                *self.model_ordering,
            ).limit(self.limit + 1))).all()

    async def paginate_object_list(
            self,
            request,
            *args,
            **kwargs: PaginationKwargs,
    ) -> list[Record]:
        self.session, self.statement = args
        self.request = request
        self.paginate_by = request.state.paginate_by
        query_params = self.request.query_params

        self.limit = self._get_limit(query_params)
        self.kwargs = kwargs
        self._prefixes_init()
        self.cursor = query_params.get('cursor')

        self._create_model_ordering()
        self._objects = self.get_objects(await self._get_query_result())
        self.object_list = self._get_object_list()

        return self.object_list

    async def get_paginated_response(self, object_list) -> CursorResponse:
        return super().get_paginated_response(object_list)


async def async_paginate_api(
        statement: Select,
        request: Request,
        session: AsyncSession,
        paginate_by: int = 100,
        strategy: Type[PaginationBase] = None,
        kwargs: Union[dict[str, Any], None] = None,
):
    """
    Returns pagination object for given strategy.

    :param statement: sqlalchemy selectable select
    :param request: fastapi Request object.
    :param session: async session object
    :param paginate_by: number of objects per page
    :param strategy: pagination strategy object
    :param kwargs: optional params passed to strategy'/s paginate_object_list method
    """
    paginator = AsyncPaginatorAPI(
        statement=statement,
        request=request,
        session=session,
        strategy=strategy,
        paginate_by=paginate_by,
        kwargs=kwargs,
    )
    return await paginator.strategy_response()
